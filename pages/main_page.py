from pages.base_page import BasePage
from locator.main_page_locator import MainPageLocator


class MainPage(BasePage):
    def should_be_main_page(self):
        self.main_page_text_is_present()
        self.should_be_main_page()

    def main_page_text_is_present(self):
        auth_text = self.find_element(MainPageLocator.LOCATOR_MAIN_PAGE_TEXT).text
        check_text = 'capital.com'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'

    # def should_be_main_page(self):
    #     self.find_element(MainPageLocator.LOCATOR_FIND_JOB_FORM)Trade

    def should_be_trade_button_mp1(self):
        self.trade_button_mp1_text_is_present()
        self.trade_button_mp1()

    def trade_button_mp1_text_is_present(self):
        auth_text = self.find_element(MainPageLocator.LOCATOR_TRADE_BUTTON_MP1_TEXT).text
        check_text = 'Trade'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'

    def trade_button_mp1(self):
        trade_button_mp1 = self.find_element(
            MainPageLocator.LOCATOR_TRADE_BUTTON_MP1
        )
        trade_button_mp1.click()