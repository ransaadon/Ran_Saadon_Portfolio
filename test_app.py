import pytest
from app import app

def test_hello_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Ran Saadon, Man, 33" in response.data
