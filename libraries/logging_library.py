

def get_page(driver, page: str) -> None:
    driver.get(page)
    driver.maximize_window()

