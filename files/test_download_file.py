import os
import requests

from selene import browser, query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from files.script_os import FILES_DIR


def test_text_in_downloaded_file():
    driver_options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': FILES_DIR,
        'download.prompt_for_download': False,
    }
    driver_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(options=driver_options, service=Service(ChromeDriverManager().install()))
    browser.config.driver = driver


    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    download_url = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))

    content = requests.get(url=download_url).content

    with open(os.path.join(FILES_DIR, 'README2.rst'), 'wb') as file:
        file.write(content)

    with open('../qa_guru/tmp/README2.rst', 'r') as file:
        readme2 = file.read()
        assert 'test_answer' in readme2

    # browser.element('[data-testid="download-raw-button"]').click()
    # time.sleep(5)
