import pytest
from selene import browser


@pytest.fixture(scope="module")
def login():
    browser.open("https://app.hafi.pro/login-v2/")
    browser.element('[placeholder="Enter email"]').type("bemero7907@ikanteri.com")
    browser.element('[placeholder="Enter password"]').type("1234567890").press_enter()


def test_sidebar_search(login):
    browser.element('//div[text()="Check influencer"]/..').click()
    browser.element('[placeholder="Enter account name"]').click().type("therock")
    browser.element('.sidebar-page [href="/profile/instagram/therock"]').click()
