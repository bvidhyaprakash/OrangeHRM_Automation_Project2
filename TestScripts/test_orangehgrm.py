import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from TestData.data import Data
from Utilities.login_excel_reader import ExcelFunction
from Utilities.test_executor import perform_excel_login_test
from PageObjects.locator import Locators
from PageObjects.login_page import LoginPage
from Configurations.conftest import driver_setup
from selenium.webdriver.common.by import By
from PageObjects.admin_page import AdminPage
from PageObjects.forgetpassword_page import ForgotPasswordPage
from PageObjects.my_info_page import MyInfoPage


class Test_OrangeHRM:
    def test_login_excel(self, driver_setup):
        excel = ExcelFunction(Data.excel_file, Data.sheet_name)
        rows = excel.row_count()
        perform_excel_login_test(driver_setup, excel, rows, Data, Locators)  # Call reusable logic here
        driver_setup.quit()

    def test_home_url_loads(self, driver_setup):
        driver_setup.get(Data.url)
        assert "orangehrmlive" in driver_setup.current_url.lower()

    def test_login_fields_visible(self, driver_setup):
        login = LoginPage(driver_setup)
        login.open()
        assert login.is_visible(login.USERNAME)
        assert login.is_visible(login.PASSWORD)
        assert login.is_visible(login.login_btn)

    def test_menu_items_present(self, driver_setup):
        driver_setup.get(Data.url)
        login_page = LoginPage(driver_setup)
        login_page.open()
        login_page.login(Data.username, Data.password)
        login_page.list_of_menu_items_present()

    def test_create_user(self, driver_setup):
        driver_setup.get(Data.url)
        login_page = LoginPage(driver_setup)
        login_page.login(Data.username, Data.password)
        admin_page = AdminPage(driver_setup)
        admin_page.navigate_to_admin()
        admin_page.add_new_user(Data.new_username, Data.new_password)

    def test_user_list(self, driver_setup):
        driver_setup.get(Data.url)
        login_page = LoginPage(driver_setup)
        login_page.login(Data.username, Data.password)
        login_page.is_visible((By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Admin']"))
        driver_setup.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Admin']").click()
        user_list_table = driver_setup.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")

    def test_forgot_password_link(self, driver_setup):
        driver_setup.get(Data.url)
        forget_pwd_page = ForgotPasswordPage(driver_setup)
        forget_pwd_page.reset_password(Data.username)
        forget_pwd_page.wait_for_reset_Success_message()
        assert forget_pwd_page.reset_success_message == forget_pwd_page.get_text(forget_pwd_page.reset_success_message_locator)

    def test_my_info_access(self, driver_setup):
        driver_setup.get(Data.url)
        login_page = LoginPage(driver_setup)
        login_page.login(Data.username, Data.password)
        myinfo_page = MyInfoPage(driver_setup)
        myinfo_page.navigate_to_myinfo()
        assert myinfo_page.visibility_of_myinfo_submenus()