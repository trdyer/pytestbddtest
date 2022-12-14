"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from pytest_bdd import scenarios, given, then, parsers


# Constants

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'


# Scenarios

scenarios('../features/service.feature')


# Given Steps

@given(parsers.parse('the DuckDuckGo API is queried with "{phrase}" using "{fmt}" format'), converters={"phrase":str},target_fixture='ddg_response')
def ddg_response(phrase, fmt):
    params = {'q': phrase, 'format': fmt}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


# Then Steps

@then(parsers.parse('the response contains results for "{phrase}"'), converters={"phrase":str})
def ddg_response_contents(ddg_response, phrase):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code
