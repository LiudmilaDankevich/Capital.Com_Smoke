from locator.login_page_locator import LoginPageLocator
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open_login_page(self):
        switch_to_frame = self.find_element(LoginPageLocator.LOCATOR_SWITCH_TO_FRAME)
        switch_to_frame.switch_to_frame()
        show_login_page_text = self.find_element(LoginPageLocator.LOCATOR_SHOW_LOGIN_PAGE).text
        check_text = 'Login'
        assert show_login_page_text == check_text, f'{show_login_page_text} is not eq {check_text}'


    #     log_in_button = self.find_element(LoginPageLocator.LOCATOR_LOG_IN_BUTTON)
    #     log_in_button.click()
    # def login(self, email, passwd):
    #     email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
    #     email_field.send_keys(email)
    #     passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
    #     passwd_field.send_keys(passwd)
    #     sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
    #     sing_in_button.click()