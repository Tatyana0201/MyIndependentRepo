from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# features/steps/steps.py

def before_scenario(context, scenario):
    """Setup WebDriver before each scenario"""
    options = Options()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def after_scenario(context, scenario):
    """Quit WebDriver after each scenario"""
    context.driver.quit()

    context.driver.maximize_window()
