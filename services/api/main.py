from fastapi import FastAPI

app = FastAPI(title="Lex Intake AI")


@app.get("/")
def root():
    return {"message": "Lex Intake AI API is running"}
