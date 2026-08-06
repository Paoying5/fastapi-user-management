import pytest
import requests


BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def client():
    session = requests.Session()
    session.base_url = BASE_URL
    return session