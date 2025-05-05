from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from local API"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/hello")
def say_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}


