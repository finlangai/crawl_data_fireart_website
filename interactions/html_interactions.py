from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def click_element(driver, xpath, timeout):
    print('xpath', xpath)
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        return True
    except NoSuchElementException:
        print(f"Không tìm thấy thẻ hoặc button với xpath: {xpath}")
        return False

def select_option(driver, select_xpath, option_text, timeout):
    try:
        select_donvi = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, select_xpath))
        )
        select_donvi.click()

        option = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, f"{select_xpath}/option[text()='{option_text}']"))
        )
        option.click()
    except NoSuchElementException:
        print(f"Không tìm thấy thẻ hoặc option với text: {option_text}")
