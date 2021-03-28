from behave import *
import os
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

@given('access to the website for search linkedIn')
def step_access_main(context):
    pass

@given('enter linkedIn in search engine')
def step_search_linkedIn(context):
     sleep(2)
     WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/header/div/div[2]/div[1]/div[2]/div"))).click()

@when('click the search botton')
def step_click_search_linkedIn_button(context):
    sleep(5)
    WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[1]/section[6]/div[2]/div/div[7]/div/div/div/div/div/div/div/a/img"))).click()
    
    sleep(5)
    WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input"))).send_keys('linkedIn')
    
    sleep(5)
    WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/span[1]/div[1]"))).click()
  

@then('tthere should show the result for linkedIn Cert')
def check_linkedIn_cert_result(context):
    sleep(5)

