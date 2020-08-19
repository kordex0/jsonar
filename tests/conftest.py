import pytest


@pytest.fixture('session')
def app():
    client = TestClient(app)
