from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message": "Grace & Focus backend is live!"}

@app.post("/planner/day")
def save_plan(data: dict):
    print("Received plan:", data)
    return {"status": "saved", "data": data}
