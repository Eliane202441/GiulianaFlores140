
 # Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSelecionarprodutoSauceDemo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(5)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_selecionarprodutoSauceDemo(self):
    self.driver.get("https://www.saucedemo.com/")
    # self.driver.set_window_size(1353, 706)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, ".login_credentials_wrap-inner").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-credentials\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".login_credentials_wrap-inner").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").text == "Add to cart"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "1"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-test.allthethings()-t-shirt-(red)\"]").click()

