from time import sleep
# from features.environment import
from selenium.webdriver.common.by import By


class Login:
    BASE_URL = 'https://www.saucedemo.com/'
    WRONG_USERNAME_INPUT = (By.XPATH, '//*[@id="user-name"]')
    WRONG_PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    WRONG_CREDENTIALS_LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    WRONG_CREDENTIALS_ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    CLEAR_WRONG_USERNAME = (By.XPATH, '//*[@id="user-name"]')
    CLEAR_WRONG_PASSWORD = (By.XPATH, '//*[@id="password"]')
    NO_USERNAME_INPUT = (By.XPATH, '//*[@id="user-name"]')
    NO_PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    NO_CREDENTIALS_LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    NO_CREDENTIALS_ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    CORRECT_USER_INPUT = (By.XPATH, '//*[@id="user-name"]')
    CORRECT_PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    CONFIRMATION_MESSAGE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def __init__(self, browser):
        self.driver = browser.driver

    def close(self):
        self.driver.quit()

    def go_to(self):
        self.driver.get(f'{self.BASE_URL}')

    def wrong_username(self, username):
        wrong_username_input = self.driver.find_element(*self.WRONG_USERNAME_INPUT)
        wrong_username_input.click()
        # sleep(1)
        wrong_username_input.send_keys(username)
        # sleep(1)

    #
    def wrong_password(self, password):
        wrong_password_input = self.driver.find_element(*self.WRONG_PASSWORD_INPUT)
        wrong_password_input.click()
        # sleep(1)
        wrong_password_input.send_keys(password)
        # sleep(1)

    def wrong_credentials_login_button(self):
        wrong_credentials_login_button = self.driver.find_element(*self.WRONG_CREDENTIALS_LOGIN_BUTTON)
        wrong_credentials_login_button.click()
        # sleep(1)

    def wrong_credentials_error_message(self):
        expected_message = self.driver.find_element(*self.WRONG_CREDENTIALS_ERROR_MESSAGE).text
        actual_message = 'Epic sadface: Username and password do not match any user in this service'
        assert expected_message == actual_message, 'The message found is incorrect'

    def clear_wrong_username(self):
        clear_wrong_username = self.driver.find_element(*self.CLEAR_WRONG_USERNAME)
        clear_wrong_username.click()
        # sleep(1)
        clear_wrong_username.clear()
        # sleep(1)

    def clear_wrong_password(self):
        clear_wrong_password = self.driver.find_element(*self.CLEAR_WRONG_PASSWORD)
        clear_wrong_password.click()
        # sleep(1)
        clear_wrong_password.clear()
        # sleep(1)

    def no_username(self, no_username):
        no_username_input = self.driver.find_element(*self.NO_USERNAME_INPUT)
        no_username_input.click()
        # sleep(1)
        no_username_input.send_keys(no_username)
        # sleep(1)

    def no_password(self, no_password):
        no_password_input = self.driver.find_element(*self.NO_PASSWORD_INPUT)
        no_password_input.click()
        # sleep(1)
        no_password_input.send_keys(no_password)
        # sleep(1)

    def no_credentials_login_button(self):
        no_credentials_login_button = self.driver.find_element(*self.NO_CREDENTIALS_LOGIN_BUTTON)
        no_credentials_login_button.click()
        # sleep(1)

    def no_credentials_error_message(self):
        expected_no_credentials_message = self.driver.find_element(*self.NO_CREDENTIALS_ERROR_MESSAGE).text
        actual_no_credentials_message = 'Epic sadface: Username is required'
        assert expected_no_credentials_message == actual_no_credentials_message, 'The message found is incorrect'

    def correct_username(self, username):
        correct_username_input = self.driver.find_element(*self.CORRECT_USER_INPUT)
        correct_username_input.click()
        # sleep(1)
        correct_username_input.send_keys(username)
        # sleep(1)

    def correct_password(self, password):
        correct_password_input = self.driver.find_element(*self.CORRECT_PASSWORD_INPUT)
        correct_password_input.click()
        # sleep(1)
        correct_password_input.send_keys(password)
        # sleep(1)

    def correct_credentials_login_button(self):
        login_button_press = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button_press.click()
        # sleep(1)

    def confirmation_message(self):
        expected_message = self.driver.find_element(*self.CONFIRMATION_MESSAGE).text
        actual_message = 'Products'
        assert expected_message == actual_message, 'The message found is incorrect'
