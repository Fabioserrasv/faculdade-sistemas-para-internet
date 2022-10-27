import pytest

from entities.user import User, UserException

TEST_DATA = {
  "name" : "Teste",
  "email": "teste@teste.com",
  "password": "senhasecreta"
}

TEST_DATA_UPDATE = {
  "name" : "Teste 2",
  "email": "novoEmail@teste.com",
  "password": "123"
}

TEST_DATA_INVALID_EMAIL = ["emailinvalido", "@.", "algumacoisa@.coma.com", ";--"]

def test_create_user():
  user = User(TEST_DATA["email"], TEST_DATA["name"], TEST_DATA["password"])

  assert user.get_email() == TEST_DATA["email"]
  assert user.get_name() == TEST_DATA["name"]
  assert user.get_password() == TEST_DATA["password"]

def test_update_user():
  user = User(TEST_DATA["email"], TEST_DATA["name"], TEST_DATA["password"])
  user.set_email(TEST_DATA_UPDATE["email"])
  user.set_name(TEST_DATA_UPDATE["name"])
  user.set_password(TEST_DATA_UPDATE["password"])

  assert user.get_email() == TEST_DATA_UPDATE["email"]
  assert user.get_name() == TEST_DATA_UPDATE["name"]
  assert user.get_password() == TEST_DATA_UPDATE["password"]

@pytest.mark.parametrize("invalid_value", TEST_DATA_INVALID_EMAIL)
def test_create_user_invalid_email(invalid_value):
  with pytest.raises(UserException):
    User(invalid_value, TEST_DATA["name"], TEST_DATA["password"])
