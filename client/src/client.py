from enum import Enum

import requests

from shared.model.requests.RegisterRequest import RegisterRequest


class HTTPMethod(str, Enum):  # noqa: UP042
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


def send_request(method: HTTPMethod, path="/", data=None, params=None, headers=None):
    BASE_URL = "http://127.0.0.1:8000"
    url = BASE_URL + path

    if method == HTTPMethod.GET:
        response = requests.get(url, params=params, headers=headers)
    elif method == HTTPMethod.POST:
        response = requests.post(url, json=data, headers=headers)
    elif method == HTTPMethod.PUT:
        response = requests.put(url, json=data, headers=headers)
    elif method == HTTPMethod.PATCH:
        response = requests.patch(url, json=data, headers=headers)
    elif method == HTTPMethod.DELETE:
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f"Unsupported method: {method}")

    print(response.json())


# Good Post Request"
req = RegisterRequest(username="jimmy", age=22, password="admin123")
send_request(HTTPMethod.POST, "/register/player", data=req.model_dump())
