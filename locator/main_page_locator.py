from selenium.webdriver.common.by import By


class MainPageLocator:

    LOCATOR_SING_IN_BUTTON = (By.CLASS_NAME, 'login')
    LOCATOR_MAIN_PAGE_TEXT = (By.XPATH, '/html/body/header/div[2]/div[2]/div/div[2]/a')