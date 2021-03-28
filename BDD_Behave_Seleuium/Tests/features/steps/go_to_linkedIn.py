from behave import *
from selenium import webdriver 
import logging
from time import sleep

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

@given('access to the website')
def step_access_linkedIn(context):
    pass

@when('click the linkedIn botton ')
def step_click_linkedIn_button(context):
    sleep(1)
    context.web.find_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/section[6]/div[2]/div/div[7]/div/div/div/div/div/div/div/a/img").click()


@then('there should redirect into linkedIn page')
def check_redirect_linkedIn(context, code):
    sleep(1)
    context.driver.save_screenshot("features/reports/go_to_linkedIn.png")