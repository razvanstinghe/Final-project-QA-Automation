from time import sleep
from selenium.webdriver.common.by import By


class Cart:
    BASE_URL = 'https://www.saucedemo.com/'
    REMOVE_BUTTON_ITEM5 = (By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
    CHECKOUT_BUTTON = (By.XPATH, '//*[@id="checkout"]')
    CONFIRMATION_MESSAGE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def __init__(self, browser):
        self.driver = browser.driver

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def remove_item4(self):
        item5_button_remove = self.driver.find_element(*self.REMOVE_BUTTON_ITEM5)
        item5_button_remove.click()
        # sleep(1)

    def checkout_button(self):
        checkout_button_press = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_button_press.click()
        # sleep(1)

    def confirmation_message(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE).text
        actual_message = 'Checkout: Your Information'
        assert expected_message == actual_message, 'The message found is incorrect'

