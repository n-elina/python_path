from selene import browser

def test_valid_login():
    browser.open("https://app.hafi.pro/login-v2/")
    browser.element('[placeholder="Enter email"]').type("bemero7907@ikanteri.com")
    browser.element('[placeholder="Enter password"]').type("1234567890").press_enter()

def test_search_in_sidebar():
    browser.element()