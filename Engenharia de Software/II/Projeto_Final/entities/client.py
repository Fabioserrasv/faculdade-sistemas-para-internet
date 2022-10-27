from typing import List
from entities.phone import Phone

class ClientException(Exception):
    pass

class Client:

    def __init__(self, name: str, contacts: List[Phone], city: str, neighborhood: str, street: str):
        self.__name = name
        self.__contacts = contacts
        self.__city = city
        self.__neighborhood = neighborhood
        self.__street = street

    def set_name(self, name: str):
        self.__name = name
        
    def set_city(self, city: str):
        self.__city = city
        
    def set_neighborhood(self, neighborhood: str):
        self.__neighborhood = neighborhood

    def set_street(self, street: str):
        self.__street = street

    def add_contacts(self, contacts: Phone):
        self.__contacts.append(contacts)
        
    def get_name(self) -> str:
        return self.__name

    def get_contacts(self) -> list:
        return self.__contacts
    
    def get_city(self) -> str:
        return self.__city

    def get_neighborhood(self) -> str:
        return self.__neighborhood

    def get_street(self) -> str:
        return self.__street