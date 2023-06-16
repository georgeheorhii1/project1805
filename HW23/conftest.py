import pytest

from HW23.infrastructure.people_servicce import PeopleService


@pytest.fixture()
def people_service():
    yield PeopleService()
