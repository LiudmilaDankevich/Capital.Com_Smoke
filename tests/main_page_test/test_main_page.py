from pages.main_page import MainPage
from pages.login_page import LoginPage
from time import sleep


def test_main_page_show(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    sleep(10)
    main_page.main_page_text_is_present()
    main_page.should_be_trade_button_mp1()
    # login_page = LoginPage(browser)
    # sleep(2)
    # login_page.open_login_page()
    # sleep(2)

