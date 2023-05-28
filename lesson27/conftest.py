import pytest

from lesson27.infrastructure.people_servicce import PeopleService


@pytest.fixture()
def people_service():
    yield PeopleService()
