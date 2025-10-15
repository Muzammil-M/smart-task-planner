🧠 Smart Task Planner

Smart Task Planner is an AI-powered project and study task planner that generates meaningful, step-by-step task plans based on your goal. It can create a daily timeline with task descriptions and dependencies, using either local logic or an LLM (via OpenRouter API) for more intelligent planning.

Features

Generate a structured plan for any goal (study, project, exam, interview preparation, etc.).

Supports LLM-based reasoning for generating meaningful task descriptions.

Fallback local logic ensures a plan is always generated even without an API key.

Includes:

Task titles and descriptions

Start and end dates

Dependencies between tasks

Lightweight and easy-to-deploy FastAPI backend.

Clean, simple frontend design for interacting with the planner.

How It Works

Enter your goal (e.g., “Prepare for GATE exam in 3 days”).

The system determines the total duration from your input.

The LLM generates a daily task plan with meaningful steps.

If API fails, fallback local reasoning generates a basic plan.

The output includes tasks with:

Title

Description

Duration

Start/End Dates

Dependencies

Installation & Usage

Clone the repo:

git clone https://github.com/YOUR_USERNAME/smart-task-planner.git
cd smart-task-planner/backend


Install dependencies:

pip install -r requirements.txt


Set OpenRouter API key (optional, for better reasoning):

export OPENROUTER_API_KEY="YOUR_KEY_HERE"  # Linux/macOS
setx OPENROUTER_API_KEY "YOUR_KEY_HERE"     # Windows


Run the backend:

uvicorn main:app --reload


Open the frontend index.html in your browser and generate plans.

Deliverables

Fully functional task planner with meaningful task generation.

Frontend UI for easy interaction.

Backend logic combining LLM reasoning and fallback local logic.

GitHub repo + README (this repo).

Evaluation Focus

Task completeness & meaningful steps

Timeline logic & task dependencies

LLM reasoning and fallback logic

Clean code structure, API design, and user interface

Future Improvements

Add user authentication to save personalized plans.

Allow custom task durations beyond 1 day.

Export plans in PDF or CSV format.

Improve frontend with interactive calendar view.
