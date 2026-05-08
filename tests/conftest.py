import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    # Arrange: create an isolated HTTP client for API calls.
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def restore_activities_state():
    # Arrange: snapshot mutable in-memory state before each test.
    original_state = copy.deepcopy(activities)

    yield

    # Assert cleanup: restore state so tests never leak changes.
    activities.clear()
    activities.update(original_state)
