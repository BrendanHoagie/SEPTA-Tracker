from utilities.request import Request
import requests
import json


_VALID_REQUESTS = {}


def choose_request() -> Request:
    """Display and choose option a set of requests

    Returns:
        a Request object from the options menu
    """
    if not _VALID_REQUESTS:
        load_valid_requests()

    for k, v in _VALID_REQUESTS.items():
        print(f"{k}:\n{v}\n\n")

    requests = []
    while True:
        for i, request_name in enumerate(_VALID_REQUESTS):
            print(f"{i + 1}. {request_name}")
            requests.append(request_name)
        try:
            choice = int(input(f"Enter a number 1-{i + 1}: ")) - 1
            print(f"choice = {choice}")
            if choice < 0:
                raise ValueError
            else:
                return _VALID_REQUESTS[requests[i]]
        except Exception:
            print("Unrecognized input, please try again")


def load_valid_requests() -> None:
    global _VALID_REQUESTS

    with open("JSON_data/valid_requests.json", "r") as file:
        data = json.load(file)
        for request_name, items in data.items():
            req = Request()
            for key, value in items.items():
                match key:
                    case "url":
                        req.set_url(value)
                    case "required_parameters":
                        for param in value:
                            req.add_required_param(param)
                    case "optional_parameters":
                        for param in value:
                            req.add_optional_param(param)
            _VALID_REQUESTS[request_name] = req
