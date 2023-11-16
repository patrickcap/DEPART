from fastapi.testclient import TestClient
from app.main import app
import os
from app.api.resources.model import models
from app.api.operations.deploy_model import CURRENT_MODEL

# Setup test client
client = TestClient(app)

# Clean up database
def setup_function():
    models.clear()

# Testing the Init page GET /
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to DEPART"}

# Testing POST /models/train endpoint
def test_train():
    test_path = os.getcwd() + "/data/data.csv"
    test_params = {
        "max_depth": 10,
        "learning_rate": 0.3,
        "n_estimators": 200,
        "objective": "binary:logistic",
        "booster": "gbtree",
        "n_jobs": 2,
        "gamma": 0.1,
        "subsample": 0.63,
        "colsample_bytree": 1,
        "colsample_bylevel": 1,
        "colsample_bynode": 1,
        "reg_alpha": 1,
        "reg_lambda": 0,
        "scale_pos_weight": 1,
        "base_score": 0.5,
        "random_state": 20212004,
        "missing": 1,
        "use_label_encoder": False
        }
    response = client.post("/models/train",params={"data_file":test_path},
                           json=test_params)
    id,model = models.popitem()
    assert response.status_code == 200
    assert response.json() == {"message": "New model (" + str(id) + ") has status " + str(model.status) + "."}

# Testing GET /models/all endpoint
def test_all_models():
    response = client.get("/models/all")
    assert response.status_code == 200
    assert response.json() == ["[]"]

# Testing POST /models/upload
def test_upload():
    test_model = os.getcwd() + "/4bda08d7-70cc-4d50-bcf2-fda3a1c97b19.pkl"
    response = client.post("/models/upload",params={"model_file":test_model})
    id,model = models.popitem()
    assert response.status_code == 200
    assert response.json() == {"message":
            "Trained model (" + str(id) + ") has status " + 
            str(model.status) + "is added into models."}

# Testing PUT /deploy
def test_deploy():
    client.post("/models/upload",params={"model_file":os.getcwd() + 
                                         "/4bda08d7-70cc-4d50-bcf2-fda3a1c97b19.pkl"})
    for key in models:
       id = key
       model = models[key]
    response = client.put("/deploy",params={"model_id":str(id.hex)})
    assert response.status_code == 200
    assert CURRENT_MODEL[0] == model
    assert response.json() == {"message": "Model deployed successfully"}

# Testing DELETE /models/{model_id}
def test_delete():
    client.post("/models/upload",params={"model_file":os.getcwd() + 
                                         "/4bda08d7-70cc-4d50-bcf2-fda3a1c97b19.pkl"})
    for key in models:
       id = key
    response = client.delete("/models/"+str(id))
    assert models == {}
    assert response.status_code == 200
    assert response.json() == {"message": "Model successfully removed."}

# Testing GET /models/{model_id}
def test_get_no_export():
    client.post("/models/upload",params={"model_file":os.getcwd() + 
                                         "/4bda08d7-70cc-4d50-bcf2-fda3a1c97b19.pkl"})
    for key in models:
       id = key
       model = models[key]
    response = client.get("/models/"+str(id),params={"export":False})
    assert response.status_code == 200
    assert response.json() == {"Model status": model.status.value}

# Testing POST /predict with trained model
def test_predict_train():
    test_predict_params = {
        "destination_city_code": "KMIA",
        "sched_airlinecode": "AAL",
        "flight_type": "I",
        "sched_date_time": "2017-01-01 23:30:00"
        }
    test_path = os.getcwd() + "/data/data.csv"
    test_params = {
        "max_depth": 10,
        "learning_rate": 0.3,
        "n_estimators": 200,
        "objective": "binary:logistic",
        "booster": "gbtree",
        "n_jobs": 2,
        "gamma": 0.1,
        "subsample": 0.63,
        "colsample_bytree": 1,
        "colsample_bylevel": 1,
        "colsample_bynode": 1,
        "reg_alpha": 1,
        "reg_lambda": 0,
        "scale_pos_weight": 1,
        "base_score": 0.5,
        "random_state": 20212004,
        "missing": 1,
        "use_label_encoder": False
        }
    client.post("/models/train",params={"data_file":test_path},
                json=test_params)
    for key in models:
       id = key
    client.put("/deploy",params={"model_id":str(id.hex)})
    response = client.post("/predict", json = test_predict_params)
    assert response.status_code == 200

# Testing POST /predict with upload model
def test_predict_upload():
    test_predict_params = {
        "destination_city_code": "KMIA",
        "sched_airlinecode": "AAL",
        "flight_type": "I",
        "sched_date_time": "2017-01-01 23:30:00"
        }
    client.post("/models/upload",params={"model_file":os.getcwd() + 
                                         "/4bda08d7-70cc-4d50-bcf2-fda3a1c97b19.pkl"})
    for key in models:
       id = key
    client.put("/deploy",params={"model_id":str(id.hex)})
    response = client.post("/predict", json = test_predict_params)
    assert response.status_code == 200