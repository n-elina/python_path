from selene import browser
from selene import have
from selene import command


def test_student_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('YA')
    browser.element('#userEmail').type('name@example.com')

    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()

    browser.element('#userNumber').type('1234567891')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1999')
    browser.element(f'.react-datepicker__day--0{11}').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).perform(
        command.js.scroll_into_view
    ).click()

    browser.element('#currentAddress').type('Moscowskaya Street 18')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            '',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
