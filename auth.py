from fastapi import FastAPI, Depends, HTTPException, Header
import os
app = FastAPI()

# Replace with your actual keys
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECURITY_KEY = os.getenv("SECURITY_KEY")

def authenticate(access_key: str = Header(None), security_key: str = Header(None)):
    if access_key != ACCESS_KEY or security_key != SECURITY_KEY:
        raise HTTPException(status_code=401, detail="Invalid API keys")
    return True

@app.get("/secure-data")
def get_secure_data(auth: bool = Depends(authenticate)):
    return {"message": "Access granted!", "data": "Sensitive Information"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)