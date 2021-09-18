from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    """Простой эндпоинт для проверки работоспособности
    """
    return {"message": "All right!"}
