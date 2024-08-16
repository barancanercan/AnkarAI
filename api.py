import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pydantic import BaseModel

from ankarai import chain  # AnkarAI backend'inizi import ediyoruz

# .env dosyasını yüklüyoruz
load_dotenv()

app = FastAPI()


class Query(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(query: Query):
    response = chain.invoke({"question": query.question})
    if isinstance(response, dict):
        answer = response.get("text", "Bir hata oluştu, lütfen tekrar deneyin.")
    else:
        answer = "Bir hata oluştu, lütfen tekrar deneyin."

    return {"answer": answer}


# Uvicorn ile başlatmak için
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
