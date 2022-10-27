from audioop import add
from typing import List
from entities.client import Client
from entities.equipment import Equipment
from entities.service import Service
from entities.service_order_status import ServiceOrderStatus

class ServiceOrderException(Exception):
  pass

class ServiceOrder:

  def __init__(self, status: ServiceOrderStatus, client: Client, services: List[Service], equipments: List[Equipment], additional_value: float, comments: str):
      self.__check_additional_value(additional_value)    
      self.__status = status
      self.__client = client
      self.__services = services
      self.__equipments = equipments
      self.__additional_value = additional_value
      self.__comments = comments


  def set_status(self, status:ServiceOrderStatus): 
    self.__status = status

  def set_client(self, client:Client):
    self.__client = client

  def add_service(self, service: Service):
    self.__services.append(service)

  def add_equipment(self, equipment: Equipment):
    self.__equipments.append(equipment)

  def set_additional_value(self, av: float):
    self.__check_additional_value(av)
    self.__additional_value = av
  
  def set_comments(self, comments: str):
    self.__comments = comments
  
  def get_status(self) -> ServiceOrderStatus:
    return self.__status
  
  def get_client(self) -> Client:
    return self.__client
  
  def get_services(self) -> List[Service]:
    return self.__services
  
  def get_equipments(self) -> List[Equipment]:
    return self.__equipments
  
  def get_additional_value(self) -> float:
    return self.__additional_value
  
  def get_comments(self) -> str:
    return self.__comments
  
  def __check_additional_value(self, value:float) -> bool:
    if value < 0:
      raise ServiceOrderException('Additional value must be a positive number.')
    
