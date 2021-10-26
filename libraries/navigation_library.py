from selenium.webdriver.common.by import By


def find_by_xpath(driver, xpath: str):
    element = driver.find_element(By.XPATH, xpath)
    return element


def change_window(driver, handle: int) -> None:
    driver.switch_to.window(driver.window_handles[handle])
