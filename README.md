# DEPART (Delay Estimation and Prediction for Aircraft Routing and Times)
DEPART is an end-to-end machine learning project with the aim of predicting the probability of delay for a given flight departing from Arturo Merino Benitez International (SCL) Airport. Given real-world airline data for SCL Airport, the overarching goals are to explore the data, train, evaluate, and select a suitable machine leanring model, and create a production-grade, scalable API for serving the model.

## Prerequisites
- **Python**==3.10
    - Please refer to the ```requirements.txt``` file for detailed information of required Python libraries and their respective versions.

## Quick Start
1. Clone this repository.
    ```
    git clone https://github.com/patrickcap/DEPART.git
    ```
2. Navigate to the "scripts" directory.
    ```
    cd scripts
    ```
3. Launch the API.
    ```
    ./launch_api.sh
    ```

## Documentation
See [DEPART's Documentation](https://patrickcap.github.io/DEPART/index.html#) for more information about how to install and use this tool as well as the development and design processes.

## Project Structure:
- **app**: Production ready code.
- **briefing**: Project tasking and completion expectations.
- **data**: Data used for unit and integration testing.
- **model**: Data pre-processing and model creation.
- **research**: Load and inspect data prior to development.
- **scripts**: Automated Bash scripts.
- **venv**: Virtual environment libraries and scripts.
