import pytest
from selene import browser
# from selenium import webdriver



@pytest.fixture
def open_browser():
   browser.open('https://demoqa.com/automation-practice-form')
   yield
   browser.quit()
