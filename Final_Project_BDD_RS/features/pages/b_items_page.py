from time import sleep
from selenium.webdriver.common.by import By


class Select:
    BASE_URL = 'https://www.saucedemo.com/'
    FILTER_BUTTON_Z_A = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    Z_TO_A_BUTTON = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
    CHECK_ITEM_Z_A = (By.XPATH, '//*[@id="item_3_title_link"]/div')
    FILTER_BUTTON_A_Z = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    A_TO_Z_BUTTON = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]')
    CHECK_ITEM_A_Z = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    ADD_BUTTON_ITEM1 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    ADD_BUTTON_ITEM2 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    ADD_BUTTON_ITEM4 = (By.XPATH, '//*[@name="add-to-cart-sauce-labs-bike-light"]')
    REMOVE_BUTTON_ITEM2 = (By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
    ADD_BUTTON_ITEM5 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    CART_BUTTON = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CONFIRMATION_MESSAGE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def __init__(self, browser):
        self.driver = browser.driver

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def filter_items_z_a(self):
        filter_button = self.driver.find_element(*self.FILTER_BUTTON_Z_A)
        filter_button.click()
        # sleep(1)

    def z_a_button(self):
        selection_z_a = self.driver.find_element(*self.Z_TO_A_BUTTON)
        selection_z_a.click()
        # sleep(1)

    def check_item_z_a(self):
        expected_z_a = self.driver.find_element(*self.CHECK_ITEM_Z_A).text
        actual_z_a = 'Test.allTheThings() T-Shirt (Red)'
        assert expected_z_a == actual_z_a, 'The Z to A filtering is not correct'

    def filter_items_a_z(self):
        filter_button = self.driver.find_element(*self.FILTER_BUTTON_A_Z)
        filter_button.click()
        # sleep(1)

    def a_z_button(self):
        selection_a_z = self.driver.find_element(*self.A_TO_Z_BUTTON)
        selection_a_z.click()
        # sleep(1)

    def check_item_a_z(self):
        expected_a_z = self.driver.find_element(*self.CHECK_ITEM_A_Z).text
        actual_a_z = 'Sauce Labs Backpack'
        assert expected_a_z == actual_a_z, 'The A to Z filtering is not correct'

    def add_item1(self):
        item1_button = self.driver.find_element(*self.ADD_BUTTON_ITEM1)
        item1_button.click()
        # sleep(1)

    def add_item2(self):
        item2_button = self.driver.find_element(*self.ADD_BUTTON_ITEM2)
        item2_button.click()
        # sleep(1)

    def add_item4(self):
        item3_button = self.driver.find_element(*self.ADD_BUTTON_ITEM4)
        item3_button.click()
        # sleep(1)

    def remove_item2(self):
        item2_button_remove = self.driver.find_element(*self.REMOVE_BUTTON_ITEM2)
        item2_button_remove.click()
        # sleep(1)

    def add_item5(self):
        item4_button = self.driver.find_element(*self.ADD_BUTTON_ITEM5)
        item4_button.click()
        # sleep(1)

    def cart_button(self):
        cart_button_press = self.driver.find_element(*self.CART_BUTTON)
        cart_button_press.click()
        # sleep(1)

    def confirmation_message(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE).text
        actual_message = 'Your Cart'
        assert expected_message == actual_message, 'The message found is incorrect'
