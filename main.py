from fastapi import FastAPI

app = FastAPI()

VERSION = "1.1.0"

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
def dev2234523():
    return {"status": "dev2 - dev3 modified"}  

@app.get("/dev3")
def dev3():
    return {"status": "dev3"}    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8111, log_level="info")