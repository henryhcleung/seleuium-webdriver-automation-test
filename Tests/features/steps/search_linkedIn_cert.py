from behave import *
import os
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
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

    sleep(5)
    input = context.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input")
    sleep(2)
    input.send_keys('linkedIn')
    sleep(2)
    input.send_keys(Keys.RETURN)


@when('click the search botton')
def step_click_search_linkedIn_button(context):
    pass

@then('there should show the result for linkedIn Cert')
def check_linkedIn_cert_result(context):
    elem = context.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/div[2]/div/div")
    context.assertNotEqual(str(elem.text), "linkedIn")



