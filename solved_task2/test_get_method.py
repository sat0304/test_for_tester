from http import HTTPStatus
from urllib.request import urlopen

import pytest


endpoint = '/Ivan'
body = f'Hello, {endpoint[1:]}'
length = len(body)
content_type = 'text/html'
status_ok = HTTPStatus.OK


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 8080)


def test_status(httpserver):
    httpserver.expect_request(endpoint, method="GET").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response.status_code
    assert status_ok == result


def test_content_type(httpserver):
    httpserver.expect_request(endpoint, method="GET").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response['content-type']
    assert content_type == result


def test_body(httpserver):
    httpserver.expect_request(endpoint, method="GET").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response.read().decode()
    assert body == result


def test_body_length(httpserver):
    httpserver.expect_request(endpoint, method="GET").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response['Content-Length']
    assert length == result
