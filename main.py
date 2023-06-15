from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def prueba():
    return {"message": "hello world from FastAPI"}
