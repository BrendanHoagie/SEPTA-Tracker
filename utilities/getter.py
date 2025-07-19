from utilities.request import Request
import requests
import json


_VALID_REQUESTS_PATH = "JSON_data/valid_requests.json"
_VALID_REQUESTS = {}


def choose_request() -> Request:
    """Display and choose option a set of requests

    Returns:
        a Request object from the options menu
    """
    if not _VALID_REQUESTS:
        load_valid_requests()

    requests = []
    while True:
        for i, request_name in enumerate(_VALID_REQUESTS):
            print(f"{i + 1}. {request_name}")
            requests.append(request_name)
        try:
            choice = int(input(f"Enter a number 1-{i + 1}: ")) - 1
            if choice < 0:
                raise ValueError
            else:
                return _VALID_REQUESTS[requests[choice]]
        except Exception:
            print("Unrecognized input, please try again")


def load_valid_requests() -> None:
    """Loads valid_requests.json into global data structure"""
    global _VALID_REQUESTS

    with open(_VALID_REQUESTS_PATH, "r") as file:
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


def construct_request(req: Request) -> None:
    """Human-readable interface for making a GET request

    Args
        req: a Request object to be turned into a http get request
    """
    params = {}

    print(f"creating GET request for {req.get_url(ext_only=False)}")
    if requireds := req.get_required_params():
        print("Required params:")
        for param in requireds:
            params[param] = input(f"\tEnter {param}: ")
    if optionals := req.get_optional_params():
        print("Optional params:")
        for param in optionals:
            params[param] = input(f"\tEnter {param}: ")
    make_get_request(req, params)


def make_get_request(req: Request, params: dict[str, str]) -> None:
    try:
        response = requests.get(req.get_url(ext_only=False), params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Caught the following error: {e}")
