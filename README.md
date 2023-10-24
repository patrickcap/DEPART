# DEPART (Delay Estimation and Prediction for Aircraft Routing and Times)
DEPART is an end-to-end machine learning project with the overarching goals being to explore the data, train, evaluate, and select a suitable machine leanring model, and create a production-grade, scalable API for serving the model. The model shall predict the probability of delay for a given flight departing from Arturo Merino Benitez International (SCL) Airport given real-world airline data for this airport.

## Quick Start
1. Clone this repository using ```git clone <repository URL>```.
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
