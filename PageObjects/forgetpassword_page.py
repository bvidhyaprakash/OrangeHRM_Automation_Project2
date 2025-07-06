from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class ForgotPasswordPage(BasePage):
    link = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    username_input = (By.NAME, "username")
    reset_button = (By.XPATH, "//button[@type='submit']")
    reset_success_message_locator = (By.XPATH, "//h6[normalize-space()='Reset Password link sent successfully']")
    reset_success_message = "Reset Password link sent successfully"


    def reset_password(self, username):
        self.click(self.link)
        self.enter_text(self.username_input, username)
        self.click(self.reset_button)

    def wait_for_reset_Success_message(self):
        self.is_visible(self.reset_success_message_locator)