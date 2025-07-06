from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestData.data import Data

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    MAIN_MENU_ITEMS = (By.CLASS_NAME, "oxd-main-menu-item")
    Admin_menu = (By.XPATH, "//span[text()='Admin']")
    PIM_menu = (By.XPATH, "//span[text()='PIM']")
    Leave_menu = (By.XPATH, "//span[text()='Leave']")
    Time_menu = (By.XPATH, "//span[text()='Time']")
    Recruitment_menu = (By.XPATH, "//span[text()='Recruitment']")
    my_info_menu = (By.LINK_TEXT, "My Info")


    def open(self):
        self.driver.get(Data.url)

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.login_btn)

    def menu_items_present(self):
        expected_items = ["Admin", "PIM", "Leave", "Time", "Recruitment"]

        # Assert all expected menu items are visible
        assert self.are_all_visible(self.MAIN_MENU_ITEMS), "Not all main menu items are visible"

        actual_items = self.find_elements(self.MAIN_MENU_ITEMS)
        actual_text = [item.text.strip() for item in actual_items if item.text.strip() != ""]

        for item in expected_items:
            assert item in actual_text, f"'{item}' not found in menu items: {actual_text}"

    def list_of_menu_items_present(self):
        Admin_menu_visible = self.is_visible(self.Admin_menu)
        PIM_menu_visible = self.is_visible(self.PIM_menu)
        Leave_menu_visible = self.is_visible(self.Leave_menu)

        # Return True if all are visible
        return Admin_menu_visible and PIM_menu_visible and Leave_menu_visible

