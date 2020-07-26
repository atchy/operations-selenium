# coding: UTF-8

import time
import sys
from time import sleep
from base.browser import Browser
from base.operation import Operation as Op

class User(Browser):

  __url = ''

  __sleep_seconds = 0

  __close_at_finished = True

  @property
  def sleep_seconds(self):
    return self.__sleep_seconds

  @sleep_seconds.setter
  def sleep_seconds(self,sleep_seconds):
    self.__sleep_seconds = sleep_seconds

  @property
  def close_at_finished(self):
    return self.__close_at_finished

  @close_at_finished.setter
  def close_at_finished(self,close_at_finished):
    self.__close_at_finished = close_at_finished

  def __init__(self,url,browser='chrome',lang=''):

    super().__init__(browser)

    self.__url = url

    super().open_url(self.__url)

    # lang指定があれば、ここらでURLをゴニョゴニョする

    self.__xpaths = {}

  def login(self,account,password):
    super().send_keys_by_name('account', account)
    super().send_keys_by_name('password', password)
    super().submit_by_name('login')
  
  def do_test(self,operations):
    print('sleep_seconds:', self.__sleep_seconds)
    print('colose_at_finished:', self.__close_at_finished)
    for op in operations:
      print('---------------')
      print('operation_type:',op.desc)
      print('element_type:',op.operation_type)
      print('element_params:',op.element_type)
      print('id:',op.id)
      
      sleep(self.__sleep_seconds)

      if op.operation_type == Op.OP_SUBMIT_BTN:

        self.submit(op.element_type,op.element_params)

      elif op.operation_type  == Op.OP_CLICK_BTN:

        self.click(op.element_type,op.element_params)

      elif op.operation_type  == Op.OP_SET_TEXT:

        self.set_text(op.element_type,op.element_params)

      elif op.operation_type  == Op.OP_SET_SELECT:

        self.set_select(op.element_type,op.element_params)

      #sleep(1)
    
    if self.__close_at_finished:
      super().close()

  def submit(self,element_type,element_params):

    if element_type == Op.ELM_BY_XPATH:
      super().submit_by_xpath(element_params[0])
    elif element_type == Op.ELM_BY_NAME:
      super().submit_by_name(element_params[0])

  def click(self,element_type,element_params):

    if element_type == Op.ELM_BY_XPATH:
      super().click_by_xpath(element_params[0])
    elif element_type == Op.ELM_BY_NAME:
      super().click_by_name(element_params[0])
    elif element_type == Op.ELM_BY_ID:
      super().click_by_id(element_params[0])

  def set_text(self,element_type,element_params):

    if element_type == Op.ELM_BY_XPATH:
      super().send_keys_by_xpath(element_params[0], element_params[1])
    elif element_type == Op.ELM_BY_NAME:
      super().send_keys_by_name(element_params[0], element_params[1])
    elif element_type == Op.ELM_BY_ID:
      super().send_keys_by_id(element_params[0], element_params[1])

  def set_select(self,element_type,element_params):

    if element_type == Op.ELM_BY_NAME:
      super().select_by_name(element_params[0],element_params[1])





