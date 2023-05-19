from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    questions_num: int


@app.post("/get-questions/")
async def get_questions(item: Item):
    questions_num = item.questions_num
    # Здесь вставьте код, который будет отвечать на запрос
    return {"questions": questions_num}
