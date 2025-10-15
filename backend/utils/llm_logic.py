import os, json, re, requests
from datetime import datetime, timedelta

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_DATE = datetime(2025, 10, 15)  # fixed start date

def local_plan(goal: str, total_days: int):
    """Generates a deterministic, meaningful plan locally without API."""
    # Define example task templates per day
    example_tasks = [
        "Gather all necessary study or project materials and resources.",
        "Create a detailed schedule or outline for the goal.",
        "Start working on the most important sections first.",
        "Review progress and adjust plan as needed.",
        "Finalize work and prepare for submission or exam."
    ]
    
    tasks = []
    for i in range(1, total_days + 1):
        start = BASE_DATE + timedelta(days=i-1)
        description = example_tasks[i-1] if i-1 < len(example_tasks) else f"Work on step {i} of {goal}."
        tasks.append({
            "id": i,
            "title": f"Day {i}: {goal} - Task",
            "description": description,
            "duration": "1 day",
            "start_date": start.strftime("%Y-%m-%d"),
            "end_date": start.strftime("%Y-%m-%d"),
            "depends_on": [i-1] if i > 1 else []
        })
    return {"goal": goal, "duration_days": total_days, "tasks": tasks}

def generate_task_plan(goal: str):
    """Generates a task plan using API if available, else fallback to local plan."""
    # Extract duration from goal
    duration_match = re.search(r"(\d+)\s*(day|week|month)s?", goal.lower())
    total_days = 7
    if duration_match:
        num, unit = duration_match.groups()
        num = int(num)
        total_days = num * 7 if "week" in unit else num * 30 if "month" in unit else num

    # Use API if key exists
    if OPENROUTER_API_KEY:
        try:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }

            prompt = f"""
You are a professional project/study planner AI. Goal: "{goal}" for {total_days} day(s).
Break it into meaningful daily tasks. Each task should have:
- Title
- Specific 'description' (actionable work)
- Duration: 1 day
- Start and end date (sequential from {BASE_DATE.strftime("%Y-%m-%d")})
Return ONLY valid JSON like this:
{{
  "goal": "{goal}",
  "duration_days": {total_days},
  "tasks": [
    {{
      "id": 1,
      "title": "Task title",
      "description": "Specific work to do",
      "duration": "1 day",
      "start_date": "YYYY-MM-DD",
      "end_date": "YYYY-MM-DD",
      "depends_on": []
    }}
  ]
}}
"""

            body = {
                "model": "gpt-4o-mini",
                "temperature": 0,  # deterministic output
                "messages": [
                    {"role": "system", "content": "You are a precise JSON-only project planning assistant."},
                    {"role": "user", "content": prompt}
                ]
            }

            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body, timeout=60)
            response.raise_for_status()
            text_output = response.json()["choices"][0]["message"]["content"].strip()
            text_output = text_output.replace("```json", "").replace("```", "").strip()
            plan = json.loads(text_output)

            # Ensure depends_on is always a list
            for task in plan.get("tasks", []):
                if isinstance(task.get("depends_on"), int):
                    task["depends_on"] = [task["depends_on"]]
                elif task.get("depends_on") in [None, "", "null"]:
                    task["depends_on"] = []

            return plan
        except:
            return local_plan(goal, total_days)
    else:
        return local_plan(goal, total_days)
