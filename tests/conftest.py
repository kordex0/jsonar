import pytest
from starlette.testclient import TestClient

from rentals import main


@pytest.fixture(scope='session')
def app():
    client = TestClient(main.app)
    yield client
