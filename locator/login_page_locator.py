from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_SHOW_LOGIN_PAGE = (By.XPATH, '//*[@id="l_overlay"]/div/div[1]')
    LOCATOR_SWITCH_TO_FRAME = (By.TAG_NAME, 'iframe')
    # LOCATOR_LOG_IN_BUTTON = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[5]')
    # LOCATOR_EMAIL_FIELD = (By.XPATH, '//*[@id="login"]/div/div[1]/div/input')
    # LOCATOR_PASSWD_FIELD = (By.XPATH, '//*[@id="login"]/div/div[2]/div/input')
    # # LOCATOR_REMEMBER_ME = (By.XPATH, '// input[ @ name = "remember_me"]')
    # LOCATOR_SING_IN_BUTTON = (By.XPATH, '//*[@id="login"]/div/div[3]/a[1]')