from selenium.webdriver.common.by import By


class MainPageLocator:

    LOCATOR_SING_IN_BUTTON = (By.CLASS_NAME, 'login')
    LOCATOR_MAIN_PAGE_TEXT = (By.XPATH, '/html/body/header/div[2]/div[2]/div/div[2]/a')
    LOCATOR_TRADE_BUTTON_MP1 =(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[1]/div/div[4]'
                                         '/table/tbody[1]/tr[2]/td[4]/a')
    LOCATOR_TRADE_BUTTON_MP1_TEXT = (By.XPATH, '/html/body/div[1]/div/main/div[2]'
                                         '/div[1]/div/div[4]/table/tbody[1]/tr[1]/td[4]/a')