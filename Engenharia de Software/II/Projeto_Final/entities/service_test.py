from platform import python_branch
import pytest
from entities.item import ItemException
from entities.service import Service

TEST_DATA = {
    "value" : 72.7,
    "description": "Uma descrição de objeto para testes"
}

TEST_DATA_UPDATE = {
    "value" : 727.0,
    "description": "Nova descrição"
}

TEST_ERROR_DATA = [0, -1, -2, -3,-4] 

def test_create_service():
    service = Service(TEST_DATA["value"], TEST_DATA["description"])

    assert service.get_value() == TEST_DATA["value"]
    assert service.get_description() == TEST_DATA["description"]

def test_update_service():
    service = Service(TEST_DATA["value"], TEST_DATA["description"])
    service.set_value(TEST_DATA_UPDATE["value"])
    service.set_description(TEST_DATA_UPDATE["description"])

    assert service.get_value() == TEST_DATA_UPDATE["value"]
    assert service.get_description() == TEST_DATA_UPDATE["description"]


@pytest.mark.parametrize("invalid_value", TEST_ERROR_DATA)
def test_create_service_error_value(invalid_value):
    with pytest.raises(ItemException):
        Service(invalid_value, TEST_DATA["description"])