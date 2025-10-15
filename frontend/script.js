document.getElementById("generate").addEventListener("click", async () => {
    const goal = document.getElementById("goal").value;

    if (!goal) {
        alert("Please enter a goal!");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/generate-plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ goal })
    });

    if (!response.ok) {
        alert("Error generating plan");
        return;
    }

    const data = await response.json();
    const planDiv = document.getElementById("plan");
    planDiv.innerHTML = `<h2>Goal: ${data.goal}</h2><p>Duration: ${data.duration_days} day(s)</p>`;

    data.tasks.forEach(task => {
        planDiv.innerHTML += `
            <div class="task">
                <h3>Day ${task.id}: ${task.title}</h3>
                <p><strong>Duration:</strong> ${task.duration}</p>
                <p><strong>Work to do:</strong> ${task.description}</p>
                <p><strong>Start:</strong> ${task.start_date}, <strong>End:</strong> ${task.end_date}</p>
            </div>
        `;
    });
});
