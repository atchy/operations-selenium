# coding: UTF-8

class Operation():

  OP_NONE = 0
  OP_SUBMIT_BTN = 1
  OP_CLICK_BTN = 2
  OP_SET_TEXT = 3
  OP_GET_TEXT = 4
  OP_SET_SELECT = 5

  ELM_BY_NONE = 0
  ELM_BY_XPATH = 1
  ELM_BY_NAME = 2
  ELM_BY_ID = 3

  __operation_type = OP_NONE

  __element_type = ELM_BY_NONE

  __element_params = None

  __payload = None

  __desc = ''

  __id = ''

  @property
  def operation_type(self):
    return self.__operation_type

  @operation_type.setter
  def operation_type(self,operation_type):
    self.__operation_type = operation_type

  @property
  def element_type(self):
    return self.__element_type

  @element_type.setter
  def element_type(self,element_type):
    self.__element_type = element_type

  @property
  def element_params(self):
    return self.__element_params

  @element_params.setter
  def element_params(self,element_params):
    self.__element_params = element_params

  @property
  def payload(self):
    return self.__payload

  @payload.setter
  def payload(self,payload):
    self.__payload = payload

  @property
  def desc(self):
    return self.__desc

  @desc.setter
  def desc(self,desc):
    self.__desc = desc

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self,id):
    self.__id = id


  def __init__(self,desc,operation_type,element_type,element_params,payload=None,id=''):
    self.__operation_type = operation_type
    self.__element_type = element_type
    self.__element_params = element_params
    self.__desc = desc
    self.__payload = payload
    self.__id = id

