from fastapi import FastAPI

app = FastAPI(
    title="DepBotPy",
    version="0.1.0",
)


@app.get("/")
def hello():
    return {"msg": "Hello FastAPI🚀"}
