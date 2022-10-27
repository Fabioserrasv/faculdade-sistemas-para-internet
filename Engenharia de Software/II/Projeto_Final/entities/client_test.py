import pytest

from entities.client import Client
from entities.equipment_test import TEST_DATA_UPDATE
from entities.phone import Phone

TEST_DATA = {
	"name" : "Cliente 1",
	"contacts" : [Phone('48 9 9999-9999'), Phone('48 9 9999-9998'), Phone('48 9 9999-9997')],
	"city" : "Imbituba",
	"neighborhood": "Centro",
	"street" : "Rua do Inferno"
}

TEST_DATA_UPDATE = {
	"name" : "Cliente 2"
}

def test_create_client():
	client = Client(TEST_DATA["name"], TEST_DATA["contacts"], TEST_DATA["city"], TEST_DATA["neighborhood"], TEST_DATA["street"])
	
	assert client.get_name() == TEST_DATA["name"]
	assert client.get_contacts() == TEST_DATA["contacts"]
	assert client.get_city() == TEST_DATA["city"]
	assert client.get_neighborhood() == TEST_DATA["neighborhood"]
	assert client.get_street() == TEST_DATA["street"]

def test_update_client():
	client = Client(TEST_DATA["name"], TEST_DATA["contacts"], TEST_DATA["city"], TEST_DATA["neighborhood"], TEST_DATA["street"])
	client.set_name(TEST_DATA_UPDATE["name"])
 
	assert client.get_name() == TEST_DATA_UPDATE["name"]