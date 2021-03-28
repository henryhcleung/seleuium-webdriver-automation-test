from selenium import webdriver 
from time import sleep

def before_all(context):
    context.driver = webdriver.Chrome("/Users/henryleung/Desktop/WebDriver/chromedriver")
    context.driver.get("https://sites.google.com/view/henry-leung-hk/")

def after_all(context):
    # context.driver.quit()
    sleep(2)