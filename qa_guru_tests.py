from selene import browser, have


def test_valid_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('ionov.kos@gmail.com')
    browser.element('[name="password"]').type('NLtm~so~ZJS3').press_enter()
    browser.element('.page-header').should(have.text('Course list'))
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.logined-form').should(have.text('Konstantin'))
    browser.close()


def test_wrong_password_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('ionov.kos@gmail.com')
    browser.element('[name="password"]').type('~so~ZJS3').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))
    browser.close()


def test_empty_password_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('ionov.kos@gmail.com')
    browser.element('[name="password"]').type('').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))
    browser.close()


def test_empty_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="password"]').type('').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))
    browser.close()
