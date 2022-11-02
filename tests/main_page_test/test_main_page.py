from pages.main_page import MainPage
from time import sleep


def test_main_page_show(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    sleep(10)
    main_page.main_page_text_is_present()

    # main_page.open_login_page()