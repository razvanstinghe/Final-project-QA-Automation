from behave import *


@Given('I am on the home page')
def step_impl(context):
    context.login_page.go_to()


@When('I click and type-in invalid username "{username}"')
def step_impl(context, username):
    context.login_page.wrong_username(username)


@When('I click and type-in invalid password "{password}"')
def step_impl(context, password):
    context.login_page.wrong_password(password)


@When('I click on the LOGIN button with wrong credentials')
def step_impl(context):
    context.login_page.wrong_credentials_login_button()
    context.login_page.clear_wrong_username()
    context.login_page.clear_wrong_password()


@Then('I check the error message:Epic sadface: Username and password do not match any user in this service')
def step_impl(context):
    context.login_page.wrong_credentials_error_message()


@When('I leave the username field empty')
def step_impl(context):
    no_username = ''
    context.login_page.wrong_username(no_username)


@When('I leave the password field empty')
def step_impl(context):
    no_password = ''
    context.login_page.no_password(no_password)


@When('I click on the LOGIN button with the empty credentials')
def step_impl(context):
    context.login_page.no_credentials_login_button()


@Then('I check the error message: Epic sadface: Username is required')
def step_impl(context):
    context.login_page.no_credentials_error_message()


@When('I type in a valid username')
def step_impl(context):
    correct_username = 'standard_user'
    context.login_page.correct_username(correct_username)


@When('I type in a valid password')
def step_impl(context):
    correct_password = 'secret_sauce'
    context.login_page.correct_password(correct_password)


@When('I click on the LOGIN button with the valid credentials')
def step_impl(context):
    context.login_page.correct_credentials_login_button()


@Then('I check the confirmation message: Products')
def step_impl(context):
    context.login_page.confirmation_message()
