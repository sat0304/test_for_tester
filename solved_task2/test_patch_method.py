from http import HTTPStatus
from urllib.request import urlopen

import pytest


endpoint = '/Ivan'
body = 'Invalid method'
length = len(body)
content_type = 'text/html'
allowed_method = 'GET, HEAD'
status_405 = HTTPStatus.METHOD_NOT_ALLOWED


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 8080)


def test_status(httpserver):
    httpserver.expect_request(endpoint, method="PATCH").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response.status_code
    assert status_405 == result


def test_content_type(httpserver):
    httpserver.expect_request(endpoint, method="PATCH").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response['content-type']
    assert content_type == result


def test_body(httpserver):
    httpserver.expect_request(endpoint, method="PATCH").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response.read().decode()
    assert body == result


def test_body_length(httpserver):
    httpserver.expect_request(endpoint, method="PATCH").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response['Content-Length']
    assert length == result


def test_body_length(httpserver):
    httpserver.expect_request(endpoint, method="PATCH").respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response['Allow']
    assert allowed_method == result
