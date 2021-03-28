# from behave import *
# import os
# import logging
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains

# #logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M',
#                     handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

# @given('access to the website')
# def step_access_linkedIn(context):
#     pass

# @when('click the linkedIn botton')
# def step_click_linkedIn_button(context):
#     # linkedInButton = context.driver.find_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/section[6]/div[2]/div/div[7]/div/div/div/div/div/div/div/a/img")
#     # linkedInButton.click()
#     sleep(2)
#     WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[1]/section[6]/div[2]/div/div[7]/div/div/div/div/div/div/div/a/img"))).click()

# @then('there should redirect into linkedIn page')
# def check_redirect_linkedIn(context):
#     sleep(5)

