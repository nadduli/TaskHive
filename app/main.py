import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
def health_check():
    """Checks the health of the application"""
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
