# SEPTA Tracker 

## Created By
Brendan Hoag <realbrendanhoag@gmail.com>

## Version 1.0

## About
General project to track the live positions of all trolley, septa regional rail, market-frankford, and broad st line trains. The goal of this project is to eventually create a pcb with LEDs representing every station in the SEPTA network.

# What's Included:
- `main.py`: the entry point of the application
- `utilities/`: folder containing utilities used in execution
    - `getter.py`: file that contains all GET request functionality
    - `timer.py`: file that contains the `timer` object, used to run functions periodically

## Dependencies
- python3
- requests library (`pip install requests`)
