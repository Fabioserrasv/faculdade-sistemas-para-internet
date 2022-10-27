import pytest
from entities.phone import Phone

TEST_DATA = "(48) 9 9999-9999"
TEST_DATA_UPDATE = "(48) 9 9999-1234"

def test_create_phone():
    contact = Phone(TEST_DATA)

    assert contact.get_number() == TEST_DATA

def test_update_phone():
    contact = Phone(TEST_DATA)
    contact.set_number(TEST_DATA_UPDATE)

    assert contact.get_number() == TEST_DATA_UPDATE
