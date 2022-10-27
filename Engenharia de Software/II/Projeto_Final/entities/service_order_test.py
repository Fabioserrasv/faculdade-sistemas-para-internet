import pytest
from entities.client import Client
from entities.equipment import Equipment
from entities.phone import Phone
from entities.service import Service
from entities.service_order import ServiceOrder, ServiceOrderException
from entities.service_order_status import ServiceOrderStatus

CLIENT_DATA = {
    "name": "Cliente 1",
    "contacts": [Phone('48 9 9999-9999'), Phone('48 9 9999-9998'), Phone('48 9 9999-9997')],
    "city": "Imbituba",
    "neighborhood": "Centro",
    "street": "Rua do Inferno"
}

TEST_DATA = {
    "status": ServiceOrderStatus.PENDING,
    "client": Client(CLIENT_DATA["name"], CLIENT_DATA["contacts"], CLIENT_DATA["city"], CLIENT_DATA["neighborhood"], CLIENT_DATA["street"]),
    "services": [Service(2.50, 'Apertar Parafuso')],
    "equipments": [Equipment(0.10, 'Parafuso')],
    "additional_value": 200,
    "comments": "Comentário"
}

ADDV_ERROR = [-1, -2, -3, 5]


def test_create_service_order():
    os = ServiceOrder(TEST_DATA["status"], TEST_DATA["client"], TEST_DATA["services"],
                      TEST_DATA["equipments"], TEST_DATA["additional_value"], TEST_DATA["comments"])

    assert os.get_status() == TEST_DATA["status"]
    assert os.get_client() == TEST_DATA["client"]
    assert os.get_services() == TEST_DATA["services"]
    assert os.get_equipments() == TEST_DATA["equipments"]
    assert os.get_additional_value() == TEST_DATA["additional_value"]
    assert os.get_comments() == TEST_DATA["comments"]


@pytest.mark.parametrize("invalid_value", ADDV_ERROR)
def test_set_wrong_additional_value(invalid_value):
    os = ServiceOrder(TEST_DATA["status"], TEST_DATA["client"], TEST_DATA["services"],
                      TEST_DATA["equipments"], TEST_DATA["additional_value"], TEST_DATA["comments"])

    with pytest.raises(ServiceOrderException):
        os.set_additional_value(invalid_value)
