import os
import uvicorn

from fastapi import FastAPI, APIRouter
from typing import Final

from api.operations.create_prediction import prediction_router

BASE_PATH: Final[str] = '/v1'
app = FastAPI()
router = APIRouter()
router.prefix = BASE_PATH

app.include_router(router)
app.include_router(prediction_router)

if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    uvicorn.run(app=app, port=port)