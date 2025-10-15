from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import llm_logic

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class PlanRequest(BaseModel):
    goal: str

@app.post("/generate-plan")
def generate_plan(request: PlanRequest):
    try:
    
        plan = llm_logic.generate_task_plan(request.goal)
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
