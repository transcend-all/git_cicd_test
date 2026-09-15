from fastapi import FastAPI

app = FastAPI()

VERSION = "1.2.0"

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

@app.get("/dev2")
def dev2():
    return {"status": "dev2"}    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8111, log_level="info")