import os
from time import sleep

from selene import browser, have
from selene.support.conditions import be

def choice_date():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1930"]').click()
    browser.element('.react-datepicker__day--008').click()

def add_data():
    browser.element('#firstName').should(be.blank).type('Иван').press_enter()
    browser.element('#lastName').should(be.blank).type('Иванов').press_enter()
    browser.element('#userEmail').should(be.blank).type('ivanov@gmail.com').press_enter()
    browser.element('label[for="gender-radio-3"]').click()
    browser.element('#userNumber').should(be.blank).type('4957777777')
    choice_date()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#subjectsInput').type('c').click()
    browser.element('.subjects-auto-complete__input').element("//*[text()='Computer Science']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('cat.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Простоквашино, д. 1')
    # Добавлен скролл строницы для доступа к следующим элементам. Обычно его упаковывают в цикл для прокрутки всей страницы
    browser.execute_script("window.scrollBy(0,100)")
    browser.element('#state').click()
    browser.element('#react-select-3-input').element("//*[text()='Haryana']").click()
    browser.element('#city').click()
    browser.element('#react-select-4-input').element("//*[text()='Karnal']").click()
    browser.element('#submit').click()

def check_data():
    browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text('Иван Иванов'))
    browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text('ivanov@gmail.com'))
    browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text('Other'))
    browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text('4957777777'))
    browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.exact_text('08 June,1930'))
    browser.element("//table//td[text()='Subjects']/../td[2]").should(have.exact_text('Computer Science'))
    browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text('Reading'))
    browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text('cat.jpg'))
    browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text('Простоквашино, д. 1'))
    browser.element("//table//td[text()='State and City']/../td[2]").should(have.exact_text('Haryana Karnal'))
    browser.element('#closeLargeModal').click()

def test_enter_context(open_browser):
    add_data()
    # Проверка заполнения
    check_data()

