from behave import given, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium .webdriver.common.keys import Keys
from time import sleep



@step('Open "{env}"environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }
    context.driver.get(environments[env])


@step('T.A. Input following credentials')
def input_following_credentials(context):
    print("This is my step")

@step('T.A. Type "{text}"into "{xpath}"')
def type_text(context, text,xpath):
    print("This is my step")


# def wait_for_element():
#     return None

@step ('Click element "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH,xpath)


@step ('Click button "{name}"')
def click_button(context, name):
    buttons = {
        'Login': "//button[text()=' Login ']",
    }
    element = context.driver.find_element(By.XPATH.buttons[name])
    element.click()
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)


