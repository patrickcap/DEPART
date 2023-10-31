# Getting Started (User)

This page provides instructions for using an already-running instance of DEPART.

## Workflows

This section will provide an overview of the common workflows that are possible using DEPART.

### Workflow A: Create, Deploy, and Use a Model for Prediction

Step A.1: Create a Model
* Utilising the Swagger user interface for FastAPI, execute the `POST /models` endpoint with a path to the required dataset and any optional parameters for the model.
* After executing this request, the user will receive a unique identifier for the trained model, remember this identifier to be able to refer to this model in other API requests.

Step A.2: Check the Model [Optional]
* Once a model is created, check the performance and status of it by executing the `GET /models` endpoint with its unique identifier.
* If the model is not satisfactor, change the model parameters/data and repeat Step A.1 until it is satisfactory.

Step A.3: Export the Model [Optional]
* If the performance of the model is satisfactory, save it locally by executing the `GET /models` endpoint again but now setting the optional `export` field to `True`.

Step A.4: Deploy the Model
* Once a model has been selected, deploy it by executing the `PUT /deploy` endpoint with the unique identifier of the model, the API key specified, and an optional path to locally stored models.
* Note that if a path to a local store of models is provided, DEPART will search in that location as well as within the current API session for the specified model. If no path is provided, DEPART will only search the current session for the specified model.
* If a model cannot be found or does not have a status of `completed`, the deployment will fail.

Step A.5: Predict with the Model
* Once a model has been successfully deployed, execute the `POST /predict` endpoint with the prediction data.
* The result will be a probability of the flight (described by the prediction data) being delayed.

### Workflow B: Delete a Model

Step B.1: Delete a Model
* If a model is present within the current API session, it can be deleted by exeucting the `DELETE /models` endpoint with the unique identifier for that model.
* If the model cannoy be found, its removal will fail.


