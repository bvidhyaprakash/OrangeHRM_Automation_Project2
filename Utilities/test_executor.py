# Utilities/test_executor.py

from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_excel_login_test(driver, excel, rows, data, locators):
    driver.get(data.url)
    driver.maximize_window()
    driver.implicitly_wait(5)

    for row in range(2, rows + 1):
        username = excel.read_data(row, 2)
        password = excel.read_data(row, 3)

        if not username or not password:
            print(f"Row {row}: Missing username or password. Skipping.")
            continue

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, locators.username_locator))
        )
        element.send_keys(username)

        driver.find_element(By.NAME, locators.password_locator).send_keys(password)
        driver.find_element(By.CLASS_NAME, locators.login_button_locator).click()

        if data.dashboard_url in driver.current_url:
            print("\nSuccess: Login successful")
            excel.write_data(row, 5, datetime.now().strftime("%H:%M:%S"))
            excel.write_data(row, 6, "Vidhya Prakash")
            excel.write_data(row, 7, "Test Passed")
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.profile_dropdown_locator))
            )
            driver.find_element(By.XPATH, locators.profile_dropdown_locator).click()
            driver.find_element(By.XPATH, locators.logout_locator).click()
            sleep(2)
        elif data.url in driver.current_url:
            print("\nFail: Login failed")
            excel.write_data(row, 5, datetime.now().strftime("%H:%M:%S"))
            excel.write_data(row, 6, "Vidhya Prakash")
            excel.write_data(row, 7, "Test Failed")
            driver.refresh()
