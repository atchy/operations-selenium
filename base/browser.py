# coding: UTF-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--proxy-server="direct://"')
chrome_options.add_argument('--proxy-bypass-list=*')
chrome_options.add_argument('--start-maximized')

firefox_options = webdriver.FirefoxOptions()

CHROME_DRIVER_PATH  = './base/webdrivers/chromedriver'
FIREFOX_DRIVER_PATH = './base/webdrivers/geckodriver'

class Browser():

  driver = None

  def __init__(self,browser):
    if browser == 'chrome':
      self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
    elif browser == 'firefox':
      self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, firefox_options=firefox_options)
    
  def open_url(self,url,on_another_tab=False):
    if on_another_tab:
      self.driver.execute_script("window.open()")
      new_window = self.driver.window_handles[-1]
      self.driver.switch_to.window(new_window)
      self.driver.get(url)
    else:
      self.driver.get(url)

  def close(self):
    self.driver.close()

  def get_element_by_name(self,name):
    return self.driver.find_element_by_name(name)

  def get_element_by_id(self,id):
    return self.driver.find_element_by_id(id)

  def get_element_by_xpath(self, xpath):
    return self.driver.find_element_by_xpath(xpath)

  def send_keys_by_name(self,name,val,overwrite=True):
    
    if overwrite:
      self.get_element_by_name(name).clear()

    self.get_element_by_name(name).send_keys(val)

  def send_keys_by_id(self,id,val,overwrite=True):

    if overwrite:
      self.get_element_by_id(id).clear()

    self.get_element_by_id(id).send_keys(val)
    
  def send_keys_by_xpath(self,xpath,val,overwrite=True):

    if overwrite:
      self.get_element_by_xpath(xpath).clear()

    self.get_element_by_xpath(xpath).send_keys(val)

  def submit_by_name(self,name):
    self.get_element_by_name(name).submit()

  def submit_by_xpath(self,xpath):
    self.get_element_by_xpath(xpath).submit()

  def submit_by_id(self,id):
    self.get_element_by_id(id).submit()

  def click_by_xpath(self,xpath):
    self.get_element_by_xpath(xpath).click()

  def click_by_name(self,name):
    self.get_element_by_name(name).click()

  def click_by_id(self,id):
    self.get_element_by_id(id).click()

  def select_by_name(self,name,indexes):
    select = Select(self.get_element_by_name(name))
    for index in indexes:
      select.select_by_index(index)