import pytest
from entities.equipment import Equipment
from entities.item import ItemException

TEST_DATA = {
    "value" : 72.7,
    "description": "Uma descrição de objeto para testes"
}

TEST_DATA_UPDATE = {
    "value" : 727.0,
    "description": "Uma descrição de objeto para testes chchghgghchgccghcghcghcghcghchchchchch"
}

TEST_ERROR_DATA = [0, -1, -2, -3,-4] 

def test_create_equipment():
    equipment = Equipment(TEST_DATA["value"], TEST_DATA["description"])

    assert equipment.get_value() == TEST_DATA["value"]
    assert equipment.get_description() == TEST_DATA["description"]

def test_update_equipment():
    equipment = Equipment(TEST_DATA["value"], TEST_DATA["description"])
    equipment.set_value(TEST_DATA_UPDATE["value"])
    equipment.set_description(TEST_DATA_UPDATE["description"])

    assert equipment.get_value() == TEST_DATA_UPDATE["value"]
    assert equipment.get_description() == TEST_DATA_UPDATE["description"]

@pytest.mark.parametrize("invalid_value", TEST_ERROR_DATA)
def test_create_equipment_error_value(invalid_value):
    with pytest.raises(ItemException):
        Equipment(invalid_value, TEST_DATA["description"])

    