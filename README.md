# Flask-SQLite-App
This is a simple python Flask application that serves data frame from SQLite database.

## Description
This application fetches iris datasetfrom github, creates a local SQLite3 database and saves the data from web, then serves it on `/` and `/n` endpoints (the latter controls the number of entries in the output).

## Setup
Install the required packages:
```py
pip install -r requirements.txt
```

## Run
```sh
flask run
```
or
```
python -m flask run
```
After the initialization the port will be displayed. Head to localhost:port.

## Testing
To run unittest `python tests.py`

## Code
Code passes flake8 tests.

