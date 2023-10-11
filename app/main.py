import asyncio
import os
import random # TESTING
import uuid
import uvicorn

from fastapi import FastAPI, APIRouter
from models import PredictionParams
from typing import Final

# from app.api.operations.get_prediction import prediction_router

app = FastAPI()
BASE_PATH: Final[str] = '/v1'
router = APIRouter()
app.include_router(router)
# app.include_router(prediction_router)

predictions = []
todos = []

@app.get("/")
async def root():
    return {"message": "DEPART root"}


# Request, predict, and return the delay probability of a particular future flight.
@app.post("/predictions", status_code=200)
async def create_prediction(prediction_params: PredictionParams):
    # Pass prediction_params to the model with id model_id

    ##############################################
    # Simulating the model fetching the prediction
    await asyncio.sleep(2)
    delay_prediction: float = random.random()
    ##############################################

    prediction_id: str = str(uuid.uuid4())

    prediction = {"ML_model_id": prediction_params.ML_model_id,
                    "flight_num": prediction_params.flight_num,
                    "delay_probability": delay_prediction,
                    "id": prediction_id}

    predictions.append(prediction)
    return {"prediction": prediction}

if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    uvicorn.run(app=app, port=port)


# Retrieve a prediction that has been previously sent to be calculated.
# @app.get("/predictions/{prediction_id}")
# async def get_prediction(prediction_id: str):
#     for prediction in predictions:
#         print(prediction)
#         if prediction['id'] == prediction_id:
#             return {"delay_probability": prediction['delay_probability'],
#                     "flight_num": prediction['flight_num'],
#                     "ML_model_id": prediction['ML_model_id']}
#     return {"message": "No delay prediction found with that ID."}









# Get single prediction
# @app.get("/predictions/{prediction_id}")
# async def get_prediction(prediction_id: int):
#     for prediction in predictions:
#         if prediction.id == prediction_id:
#             return {"prediction": prediction}
#     return {"message": "Could not get, no predictions found with that ID"}


##############################


# # Get all todos
# @app.get("/todos")
# async def get_todos():
#     return {"todos": todos}

# # Get single todo
# @app.get("/todos/{todo_id}")
# async def get_todo(todo_id: int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return {"todo": todo}
#     return {"message": "Could not get, no todos found with that ID"}

# # Create a todo
# @app.post("/todos")
# async def create_todo(todo: Todo):
#     todos.append(todo)
#     return {"message": "Todo has been added"}

# # Update a todo
# @app.put("/todos")
# async def update_todo(todo_id: int, todo_obj: Todo):
#     for todo in todos:
#         if todo.id == todo_id:
#             todo.id = todo_obj.id
#             todo.item = todo_obj.item
#             return {"todo": todo}
#     return {"message": "Could not update, no todos found with that ID"}

# # Delete a todo
# @app.delete("/todos/{todo_id}")
# async def delete_todo(todo_id: int):
#     for todo in todos:
#         if todo.id == todo_id:
#             todos.remove(todo)
#             return {"message": "Todo deleted"}
#     return {"message": "Could not delete, no todos found with that ID"}
