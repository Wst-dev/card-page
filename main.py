from routers import app as api
if __name__ == "__main__":
    import uvicorn
    import os 
    server_address = os.getenv("SERVER_ADDRESS", "0.0.0.0:80")
    host, port = server_address.split(":")
    uvicorn.run(app=api, host=host, port=int(port))