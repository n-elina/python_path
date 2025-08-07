import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = "https://app.hafi.pro"

    driver_options=webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    driver_options.add_argument('--disable-gpu')

    yield

    browser.quit()
