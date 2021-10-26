import pytest
from selenium import webdriver
from libraries.logging_library import get_page
from libraries.navigation_library import find_by_xpath, change_window


def test_negative_login():
    chrome_driver = webdriver.Chrome()
    page_address = 'http://testarena.pl/demo'
    landing_page_title = 'TestArena'
    login_page_title = 'TestArena Demo'
    next_window = 1
    email_address = 'tester@testarena.pl'
    password_credentials = '123456789'

    get_page(chrome_driver, page_address)
    assert landing_page_title == chrome_driver.title
    demo_page = find_by_xpath(chrome_driver, '//a[@href="http://demo.testarena.pl/"]')
    demo_page.click()
    change_window(chrome_driver, next_window)
    assert login_page_title == chrome_driver.title
    email = find_by_xpath(chrome_driver, '//input[@id="email"]')
    email.send_keys(email_address)
    password = find_by_xpath(chrome_driver, '//input[@id="password"]')
    password.send_keys(password_credentials)
    form = find_by_xpath(chrome_driver, '//form[@method="post"]')
    form.submit()
    error_message = find_by_xpath(chrome_driver, '//div[@class="login_form_error"]').text
    error_text = 'Adres e-mail i/lub hasło są niepoprawne.'
    assert error_message == error_text
    chrome_driver.close()