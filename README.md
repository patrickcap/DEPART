# DEPART (Delay Estimation and Prediction for Aircraft Routing and Times)
DEPART is an end-to-end machine learning project with the aim of predicting the probability of delay for a given flight departing from Arturo Merino Benitez International (SCL) Airport. Given real-world airline data for SCL Airport, the overarching goals are to explore the data, train, evaluate, and select a suitable machine leanring model, and create a production-grade, scalable API for serving the model.

## Prerequisites
- **python**==3.10
    - **annotated-types**==0.6.0
    - **anyio**==3.7.1
    - **click**==8.1.7
    - **colorama**==0.4.6
    - **exceptiongroup**==1.1.3
    - **fastapi**==0.104.0
    - **h11**==0.14.0
    - **idna**==3.4
    - **joblib**==1.3.2
    - **pydantic**==2.4.2
    - **pydantic_core**==2.10.1
    - **sniffio**==1.3.0
    - **starlette**==0.27.0
    - **typing_extensions**==4.8.0
    - **uvicorn**==0.23.2

## Quick Start
1. Clone this repository using ```git clone https://github.com/patrickcap/DEPART.git```.
2. Navigate to the "scripts" directory by running ```cd scripts```.
3. Launch the API by running the command ```./launch_api.sh```.

## Project Structure:
- **app**: Production ready code.
- **briefing**: Project tasking and completion expectations.
- **data**: Data used for unit and integration testing.
- **model**: Data pre-processing and model creation.
- **research**: Load and inspect data prior to development.
- **scripts**: Automated Bash scripts.
- **venv**: Virtual environment libraries and scripts.
