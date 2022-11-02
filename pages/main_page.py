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
    #     self.find_element(MainPageLocator.LOCATOR_FIND_JOB_FORM)
    #
    #
    # def click_sing_in_button(self):
    #     sing_in_button = self.find_element(
    #         MainPageLocator.LOCATOR_SING_IN_BUTTON
    #     )
    #     sing_in_button.click()