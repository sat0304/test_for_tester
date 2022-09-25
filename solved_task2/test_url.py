from http import HTTPStatus
from urllib.request import urlopen

import pytest


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 8080)


def test_name(httpserver):
    # httpserver.expect_request("/foobar", method="GET")
    endpoint = '/Ivan'
    name = endpoint[1:]
    body = f'Hello, {name}'
    httpserver.expect_request(endpoint).respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response.read().decode()
    assert body == result

def test_query_params(httpserver):
    httpserver.expect_request("/foo", query_string="user=bar")


    def test_url_exists_at_desired_location_user(self):
        """URL-адрес существует для зарегистрированного."""
        templates_url_names = {
            settings.HOME_PAGE: HTTPStatus.OK,
            f'{settings.GROUP}{self.group.slug}/': HTTPStatus.OK,
            f'{settings.PROFILE}{self.post.author}/': HTTPStatus.OK,
            f'{settings.POSTS}{self.post.pk}/': HTTPStatus.OK,
            f'{settings.POSTS}{self.post.pk}{self.edit}': HTTPStatus.FOUND,
            f'{settings.CREATE}': HTTPStatus.OK,
            'unexist.html': HTTPStatus.NOT_FOUND,
        }
        for template, status in templates_url_names.items():
            with self.subTest(status=status):
                response = self.authorized_client.get(template)
                self.assertEqual(response.status_code, status)
                self.assertEqual(response['content-type'], 'application/json')

import requests
  
# Making a DELETE request
r = requests.delete('https://httpbin.org / delete', data ={'key':'value'})
  
# check status code for response received
# success code - 200
print(r)
  
# print content of request
print(r.json())
METHOD_NOT_ALLOWED