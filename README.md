# DEPART (Delay Estimation and Prediction for Aircraft Routing and Times)
DEPART is an end-to-end machine learning project with the aim of predicting the probability of delay for a given flight departing from Arturo Merino Benitez International (SCL) Airport. Given real-world airline data for SCL Airport, the overarching goals are to explore the data, train, evaluate, and select a suitable machine learning model, and create a production-grade, scalable API for serving the model.

## Prerequisites
- **Python**==3.10
- Please install the required Python libraries and their respective versions by running the command:
    ```
    pip install -r requirements.txt
    ```
    We would recommend that you do this inside a new virtual environment. You can use the command ```python3 -m venv <name_of_virtualenv>``` to create a virtual environment in the project directory and then activate it.

## Quick Start
1. Clone this repository.
    ```
    git clone https://github.com/patrickcap/DEPART.git
    ```
2. Navigate to the "scripts" directory within DEPART.
    ```
    cd scripts
    ```
3. Launch the API.
    ```
    ./launch_api.sh
    ```
You can use a more user-friendly view of the API that uses Swagger by navigating to ```localhost:8080/docs``` on your browser.

## Documentation
See [DEPART's Documentation](https://patrickcap.github.io/DEPART/index.html#) for more information about how to install and use this tool as well as the development and design processes.

## Project Structure:
- **app**: Production ready code.
- **briefing**: Project tasking and completion expectations.
- **data**: Data used for unit and integration testing.
- **docs**: User documentation, Sphinx files.
- **research**: Load and inspect data prior to development in a jupyter notebook.
- **scripts**: Automated Bash scripts.
