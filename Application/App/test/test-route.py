import pytest
import requests



def test_hello():
    response = requests.get('http://10.59.2.13:8082/')
    assert response.status_code == 200

def test_poulet():
    response = requests.get('http://10.59.2.13:8082/')
    assert response.status_code == 200

