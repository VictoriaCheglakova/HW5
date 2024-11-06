import pytest
from selene import browser
from selenium import webdriver



@pytest.fixture
def open_browser():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-notifications')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-infobars')
    # options.add_argument('--enable-automation')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-setuid-sandbox')
    # browser.config.driver_options = options
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()