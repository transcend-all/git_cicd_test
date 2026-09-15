from fastapi import FastAPI

app = FastAPI()

VERSION = "2.0.0"

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

@app.get("/dev4")
def dev4():
    return {"status": "dev4"} 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8111, log_level="info")