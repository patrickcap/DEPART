"""
Aggregates all API routers and starts the API.
"""

import os
import uvicorn

from fastapi import FastAPI, APIRouter
from typing import Final

from api.operations.create_prediction import prediction_router
from api.operations.create_model import create_model_router
from api.operations.remove_model import remove_model_router
from api.operations.check_model import check_model_router
from api.operations.deploy_model import deploy_model_router

# Allow versioning of the API via the URI path
BASE_PATH: Final[str] = '/v1'
app = FastAPI()
router = APIRouter()
router.prefix = BASE_PATH

# Add endpoints connected to other routers to this router.
app.include_router(router)
app.include_router(prediction_router)
app.include_router(create_model_router)
app.include_router(remove_model_router)
app.include_router(check_model_router)
app.include_router(deploy_model_router)

# Run the API
if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    uvicorn.run(app=app, port=port)
