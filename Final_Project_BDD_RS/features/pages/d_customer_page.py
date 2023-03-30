from time import sleep
from selenium.webdriver.common.by import By


class CostumerDetails:
    BASE_URL = 'https://www.saucedemo.com/'
    FIRST_NAME_1 = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_1 = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE_1 = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON_1 = (By.XPATH, '//*[@id="continue"]')
    CONFIRMATION_MESSAGE_1 = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')

    FIRST_NAME_2 = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_2 = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE_2 = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON_2 = (By.XPATH, '//*[@id="continue"]')
    CONFIRMATION_MESSAGE_2 = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')

    FIRST_NAME_3 = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_3 = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE_3 = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON_3 = (By.XPATH, '//*[@id="continue"]')
    CONFIRMATION_MESSAGE_3 = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')

    FIRST_NAME_4 = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_4 = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE_4 = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON_4 = (By.XPATH, '//*[@id="continue"]')
    CONFIRMATION_MESSAGE_4 = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    FIRST_NAME_5 = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_5 = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE_5 = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON_5 = (By.XPATH, '//*[@id="continue"]')
    CONFIRMATION_MESSAGE_5 = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def __init__(self, browser):
        self.driver = browser.driver

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def first_name_1(self, first_name):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_1)
        first_name_input.click()
        # sleep(1)
        first_name_input.send_keys(first_name)
        # sleep(1)

    def last_name_1(self, last_name):
        last_name_input = self.driver.find_element(*self.LAST_NAME_1)
        last_name_input.click()
        # sleep(1)
        last_name_input.send_keys(last_name)
        # sleep(1)

    def zip_code_1(self, zip_code):
        zip_code_input = self.driver.find_element(*self.ZIP_CODE_1)
        zip_code_input.click()
        # sleep(1)
        zip_code_input.send_keys(zip_code)
        # sleep(1)

    def continue_button_1(self):
        continue_button_press = self.driver.find_element(*self.CONTINUE_BUTTON_1)
        continue_button_press.click()
        # sleep(1)

    def confirmation_message_1(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE_1).text
        actual_message = 'Error: First Name is required'
        assert expected_message == actual_message, 'The message found is incorrect'

    def first_name_2(self, first_name):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_2)
        first_name_input.click()
        # sleep(1)
        first_name_input.send_keys(first_name)
        # sleep(1)

    def last_name_2(self, last_name):
        last_name_input = self.driver.find_element(*self.LAST_NAME_2)
        last_name_input.click()
        # sleep(1)
        last_name_input.send_keys(last_name)
        # sleep(1)

    def zip_code_2(self, zip_code):
        zip_code_input = self.driver.find_element(*self.ZIP_CODE_2)
        zip_code_input.click()
        # sleep(1)
        zip_code_input.send_keys(zip_code)
        # sleep(1)

    def continue_button_2(self):
        continue_button_press = self.driver.find_element(*self.CONTINUE_BUTTON_2)
        continue_button_press.click()
        # sleep(1)

    def confirmation_message_2(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE_2).text
        actual_message = 'Error: Last Name is required'
        assert expected_message == actual_message, 'The message found is incorrect'

    def first_name_3(self, first_name):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_3)
        first_name_input.click()
        # sleep(1)
        first_name_input.send_keys(first_name)
        # sleep(1)

    def last_name_3(self, last_name):
        last_name_input = self.driver.find_element(*self.LAST_NAME_3)
        last_name_input.click()
        # sleep(1)
        last_name_input.send_keys(last_name)
        # sleep(1)

    def zip_code_3(self, zip_code):
        zip_code_input = self.driver.find_element(*self.ZIP_CODE_3)
        zip_code_input.click()
        # sleep(1)
        zip_code_input.send_keys(zip_code)
        # sleep(1)

    def continue_button_3(self):
        continue_button_press = self.driver.find_element(*self.CONTINUE_BUTTON_3)
        continue_button_press.click()
        # sleep(1)

    def confirmation_message_3(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE_3).text
        actual_message = 'Error: Postal Code is required'
        assert expected_message == actual_message, 'The message found is incorrect'

    def first_name_4(self, first_name):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_4)
        first_name_input.click()
        # sleep(1)
        first_name_input.send_keys(first_name)
        # sleep(1)

    def last_name_4(self, last_name):
        last_name_input = self.driver.find_element(*self.LAST_NAME_4)
        last_name_input.click()
        # sleep(1)
        last_name_input.send_keys(last_name)
        # sleep(1)

    def zip_code_4(self, zip_code):
        zip_code_input = self.driver.find_element(*self.ZIP_CODE_4)
        zip_code_input.click()
        # sleep(1)
        zip_code_input.send_keys(zip_code)
        # sleep(1)

    def continue_button_4(self):
        continue_button_press = self.driver.find_element(*self.CONTINUE_BUTTON_4)
        continue_button_press.click()
        # sleep(1)

    def confirmation_message_4(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE_4).text
        actual_message = 'Checkout: Overview'
        assert expected_message != actual_message, 'WARNING! First Name and Last Name are written with digits only and Zip Code is written with letters only!'

    def first_name_5(self, first_name):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_5)
        first_name_input.click()
        # sleep(1)
        first_name_input.send_keys(first_name)
        # sleep(1)

    def last_name_5(self, last_name):
        last_name_input = self.driver.find_element(*self.LAST_NAME_5)
        last_name_input.click()
        # sleep(1)
        last_name_input.send_keys(last_name)
        # sleep(1)

    def zip_code_5(self, zip_code):
        zip_code_input = self.driver.find_element(*self.ZIP_CODE_5)
        zip_code_input.click()
        # sleep(1)
        zip_code_input.send_keys(zip_code)
        # sleep(1)

    def continue_button_5(self):
        continue_button_press = self.driver.find_element(*self.CONTINUE_BUTTON_5)
        continue_button_press.click()
        # sleep(1)

    def confirmation_message_5(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE_5).text
        actual_message = 'Checkout: Overview'
        assert expected_message == actual_message, 'The message found is incorrect'
