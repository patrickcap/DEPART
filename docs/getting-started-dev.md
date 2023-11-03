# Getting Started (Developer)

This page provides instructions for installing and running a development environment of DEPART, as well as advice for extending the existing code.

## Prerequisites

## Cloning the Repository

1. Open a termainal and navigate to a directory where you wish to store DEPART.
2. Run the following command to clone the repository to your desired directory.

```
git clone https://github.com/patrickcap/DEPART
```

3. Check that the repository has been successfully cloned by switching to it's directory.
```
cd DEPART
```

## Running the API
1. Once inside the cloned DEPART directory, navigate to the ```/scripts``` directory.
```
cd scripts
```
2. Run the script to launch the API.
```
./launch_api.sh
```
3. A local instance of the API should start running with a link provided in the terminal response to access the API.

4. Append "/docs" to the end of this URL and paste it into an internet browser. The result should be a FastAPI user interface for DEPART.
