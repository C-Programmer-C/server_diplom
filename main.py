from fastapi import FastAPI
import uvicorn
from api.auth import auth_router
from fastapi.staticfiles import StaticFiles
from api.product import product_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(product_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
