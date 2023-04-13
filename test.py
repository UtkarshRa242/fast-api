from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def homepage():
    return {"Welcome to Spectre&Ross Legal Service"}
@app.get("/signup")
asyc