import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        register_form.send_keys(email)

        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_form.send_keys("2q3w4e5r6t7y")
        confirm_password_form = self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD
        )
        confirm_password_form.send_keys("2q3w4e5r6t7y")

        confirm_registration = self.browser.find_element(
            *LoginPageLocators.CONFIRM_REGISTRATION
        )
        confirm_registration.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert (
            "login" in current_url
        ), f"Expected URL to contain the word 'login', but got '{current_url}'."

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is absent."

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Register form is absent"
