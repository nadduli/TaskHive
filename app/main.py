#!/usr/bin/python3

"""
Entry point to taskhive application
"""
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/health")
def health_check():
    """Checks the health of the application"""
    return {"status": "Ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
