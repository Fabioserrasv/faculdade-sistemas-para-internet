import re
class UserException(Exception):
    pass

class User:

    def __init__(self, email: str, name: str, password: str):
        self.__validate_email(email)
        self.__email = email
        self.__name = name
        self.__password = password

    def set_name(self, name: str):
        self.__name = name

    def set_email(self, email: str):
        self.__validate_email(email)
        self.__email = email
        
    def set_password(self, password: str):
        self.__password = password
        
    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        
        return self.__email
        
    def get_password(self) -> str:
        return self.__password
    
    def check_password(self, password) -> bool:
        return self.__password == password

    def __validate_email(self, email:str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
        if not re.match(regex,email):
            raise UserException("Invalid Email.")