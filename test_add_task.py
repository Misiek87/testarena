import pytest
from selenium import webdriver
from libraries.logging_library import get_page
from libraries.navigation_library import find_by_xpath, change_window
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_new_task():
    chrome_driver = webdriver.Chrome()
    page_address = 'http://testarena.pl/demo'
    landing_page_title = 'TestArena'
    login_page_title = 'TestArena Demo'
    kokpit_page_title = 'Kokpit - TestArena Demo'
    zadania_page_title = 'Zadania - TestArena Demo'
    dodaj_page_title = 'Dodaj zadanie - TestArena Demo'
    next_window = 1
    email_address = 'administrator@testarena.pl'
    password_credentials = 'sumXQQ72$L'
    project = "Projekt Wioleta Test"

    title = "New Test Title"
    description = "Created to test Selenium framework"
    environment = "Środowisko 1/Projekt Wioleta Test"
    version = "Wersja 1 Projekt Wio"
    date = "2021-10-22 23:59"
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
    assert kokpit_page_title == chrome_driver.title
    select = Select(find_by_xpath(chrome_driver, '//select[@id="activeProject"]'))
    select.select_by_visible_text(project)
    task_page = find_by_xpath(chrome_driver, '//a[@href = "http://demo.testarena.pl/Wtest/tasks"]')
    task_page.click()
    assert zadania_page_title == chrome_driver.title
    add_page = find_by_xpath(chrome_driver, '//a[contains(text(), "Dodaj zadanie")]')
    add_page.click()
    assert dodaj_page_title == chrome_driver.title
    task_title = find_by_xpath(chrome_driver, '//input[@id="title"]')
    task_title.send_keys(title)
    task_description = find_by_xpath(chrome_driver, '//textarea[@id="description"]')
    task_description.send_keys(description)
    task_environments = find_by_xpath(chrome_driver, '//input[@id="token-input-environments"]')
    task_environments.send_keys(environment)
    time.sleep(3)
    task_environments.send_keys(Keys.ENTER)
    task_versions = find_by_xpath(chrome_driver, '//input[@id="token-input-versions"]')
    task_versions.send_keys(version)
    time.sleep(3)
    task_versions.send_keys(Keys.ENTER)
    task_date = find_by_xpath(chrome_driver, '//input[@id="dueDate"]')
    task_date.send_keys(date)
    assignment = find_by_xpath(chrome_driver, '//a[@id="j_assignToMe"]')
    assignment.click()
    save_task = find_by_xpath(chrome_driver, '//form[@action="http://demo.testarena.pl/Wtest/task_add_process"]')
    save_task.submit()
    check_page = find_by_xpath(chrome_driver, '//a[@href = "http://demo.testarena.pl/Wtest/tasks"]')
    check_page.click()
    confirm = find_by_xpath(chrome_driver, f'//td[@class="title_task_max"]').text
    assert title in confirm
    chrome_driver.close()
