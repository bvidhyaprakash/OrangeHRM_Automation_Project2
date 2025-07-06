from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class MyInfoPage(BasePage):
    my_info_menu = (By.LINK_TEXT, "My Info")
    PersonalDetails_submenu = (By.XPATH, "//a[normalize-space()='Personal Details']")
    ContactDetails_submenu = (By.XPATH, "//a[normalize-space()='Contact Details']")
    EmergencyContact_submenu = (By.XPATH, "//a[normalize-space()='Emergency Contacts']")




    def navigate_to_myinfo(self):
        self.click(self.my_info_menu)

    def visibility_of_myinfo_submenus(self):
        # Check if all submenus are visible
        personal_details_visible = self.is_visible(self.PersonalDetails_submenu)
        contact_details_visible = self.is_visible(self.ContactDetails_submenu)
        emergency_contact_visible = self.is_visible(self.EmergencyContact_submenu)

        # Return True if all are visible
        return personal_details_visible and contact_details_visible and emergency_contact_visible
