from fastapi import FastAPI

app = FastAPI()

VERSION = "1.0.0"

@app.get("/")
def home():
    return {
        "application": "Data Engineering Demo",
        "version": VERSION,
        "environment": "production"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8111, log_level="info")