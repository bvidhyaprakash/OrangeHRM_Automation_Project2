from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class AdminPage(BasePage):

    admin_menu = (By.XPATH, "//span[text()='Admin']")
    add_user_btn = (By.XPATH, "//button[text()=' Add ']")
    username_field = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    password_field = (By.XPATH, "//label[text()='Password']/../following-sibling::div/input")
    confirm_password_field = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input")
    save_button = (By.XPATH, "//button[text()=' Save ']")
    user_search_field = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    search_button = (By.XPATH, "//button[text()=' Search ']")

    def navigate_to_admin(self):
        self.click(self.admin_menu)

    def add_new_user(self, username, password):
        self.navigate_to_admin()
        self.click(self.add_user_btn)
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.enter_text(self.confirm_password_field, password)
        self.click(self.save_button)

    def search_user(self, username):
        self.navigate_to_admin()
        self.enter_text(self.user_search_field, username)
        self.click(self.search_button)