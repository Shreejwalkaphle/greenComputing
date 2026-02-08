from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate_green_score
from history_saver import save_evaluation
from history_reader import get_all_history



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EvaluationInput(BaseModel):
    hardware: str
    devices: int
    hours: float
    country: str


@app.get("/")
def home():
    return {"message": "Green Computing API is running"}


@app.post("/evaluate")
def evaluate(data: EvaluationInput):
    result = calculate_green_score(data.dict())

    # save to DB
    save_evaluation(data.dict(), result)

    return result

@app.get("/history")
def history():
    return get_all_history()
