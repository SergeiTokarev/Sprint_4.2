import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def driver():
    url = 'https://qa-scooter.praktikum-services.ru/'
    browser_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()