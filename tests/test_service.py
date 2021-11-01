import sys

sys.path.append("..")

from flask import Flask
import pytest
from src.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


def test_home(client):
    assert client.get("/").data == b"Hello, World!"
