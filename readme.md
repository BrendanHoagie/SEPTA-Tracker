# SEPTA Tracker 

## Created By
Brendan Hoag <realbrendanhoag@gmail.com>

## Version 1.0

## About
General project to track the live positions of all trolley, septa regional rail, market-frankford, and broad st line trains. The goal of this project is to eventually create a pcb with LEDs representing every station in the SEPTA network.

# What's Included:
- `main.py`: the entry point of the application
- `utilities/`: folder containing utilities used in execution
    - `getter.py`: file that contains GET request functionality
    - `timer.py`: file that contains the `timer` object, used to run functions periodically.
    - `request.py`: file that contains Request objects, simplifies working with data in `getter.py`
- `JSON_data/`: folder containing json data files:
    - `valid_requests.json`: a json file containing all http requests we care about, the url extension, required & optional arguments
- `formatting_data/`: a folder for collecting and formatting argument data. Stuff here will eventualkly become files in `JSON_data`
    - `formatted/`: folder where formatted data files are outputted
    - `raw/`: folder where raw data files are ingested from
    - `scripts/`: python scripts to convert files in `raw/` to presentable ones in `formatted/`

## Dependencies
- python3
- requests library (`pip install requests`)

## What Works
- 7/18/2025: read in request types from data files, CLI to choose request type, fill arguments, and show responses