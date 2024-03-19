import uvicorn
from fastapi import FastAPI

from model import Prompt
from Service import ask_method

app = FastAPI()


@app.get("/health")
def health():
    return {"message": "healthy"}


@app.post("/ask")
def ask(body: Prompt):
    try:
        return ask_method(body.prompt)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
