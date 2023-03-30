from time import sleep
from selenium.webdriver.common.by import By


class OrderConfirmation:
    BASE_URL = 'https://www.saucedemo.com/'
    CHECKOUT_VERIFICATION = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    MENU_CLICK = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    LOGOUT_CONFIRMATION = (By.XPATH, '//*[@id="login_credentials"]/h4')

    def __init__(self, browser):
        self.driver = browser.driver

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def checkout_verification(self):
        checkout_verification_test = self.driver.find_element(*self.CHECKOUT_VERIFICATION)
        return checkout_verification_test.text

    def menu_click(self):
        menu_click_logout = self.driver.find_element(*self.MENU_CLICK)
        menu_click_logout.click()
        # sleep(1)

    def logout_button(self):
        logout_button_press = self.driver.find_element(*self.LOGOUT_BUTTON)
        logout_button_press.click()
        # sleep(1)

    def logout_confirmation(self):
        expected_confirmation_test = self.driver.find_element(*self.LOGOUT_CONFIRMATION).text
        actual_confirmation_test = 'Accepted usernames are:'
        assert expected_confirmation_test == actual_confirmation_test, 'The message found is incorrect'
