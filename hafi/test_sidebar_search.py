import pytest
from selene import browser, be, have


@pytest.fixture(scope="function")
def login():
    browser.open("/")
    browser.element('[placeholder="Enter email"]').type("bemero7907@ikanteri.com")
    browser.element('[placeholder="Enter password"]').type("1234567890").press_enter()


def test_sidebar_search(login):
    browser.element('//div[text()="Check influencer"]/..').click()
    browser.element('input[placeholder="Enter account name"]').should(be.blank).click().type("therock")
    browser.element('.sidebar-page [href="/profile/instagram/therock"]').click()
    browser.should(have.url('https://app.hafi.pro/profile/instagram/therock'))
