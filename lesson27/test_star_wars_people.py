import pytest


@pytest.mark.parametrize('keyword, value', [('name', 'Luke Skywalker'), ('height', '172'), ('mass', '77')])
def test_check_person_1(people_service, keyword, value):
    responce = people_service.get_person(1)

    print(responce.json())
    assert responce.json()[keyword] == value
