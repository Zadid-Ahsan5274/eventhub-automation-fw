from pages.base_page import BasePage
from utils.test_data import TestData
from playwright.sync_api import Page

class RegistrationPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        self.email_text_field = page.locator("#register-email")
        self.password_text_field = page.locator("#register-password")
        self.confirm_password_text_field = page.get_by_placeholder("Repeat your password")
        self.register_button = page.locator("//button[@id='register-btn']")
        self.sign_in_link = page.locator("//a[normalize-space()='Sign in']")
        self.email = TestData.unique_email(prefix="qa") #unique email
        self.password = TestData.random_password()
        self.confirm_password = self.password

    def navigate_to_registration_page(self) -> None:
        self.page.goto("https://eventhub.rahulshettyacademy.com/register")

    def enter_email(self,email) -> None:
        self.email_text_field.fill(email)

    def enter_password(self,password) -> None:
        self.password_text_field.fill(password)

    def enter_confirm_password(self,confirm_password) -> None:
        self.confirm_password_text_field.fill(confirm_password)

    def click_register_button(self) -> None:
        self.register_button.click()

    def navigate_to_sign_in_page(self):
        self.sign_in_link.click()

    



   
    

    
        