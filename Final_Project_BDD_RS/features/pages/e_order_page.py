from time import sleep
from selenium.webdriver.common.by import By


class OrderPage:
    BASE_URL = 'https://www.saucedemo.com/'
    ITEM1_CHECK = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    ITEM4_CHECK = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
    CONFIRMATION_MESSAGE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def __init__(self, browser):
        self.driver = browser.driver

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def item1_check(self):
        item1_check = self.driver.find_element(*self.ITEM1_CHECK)
        return item1_check.text

    def item4_check(self):
        item4_check = self.driver.find_element(*self.ITEM4_CHECK)
        return item4_check.text

    def finish_button(self):
        finish_button_press = self.driver.find_element(*self.FINISH_BUTTON)
        finish_button_press.click()

    def confirmation_message(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE).text
        actual_message = 'Checkout: Complete!'
        assert expected_message == actual_message, 'The message found is incorrect'