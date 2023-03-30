from behave import *


@Given('I am on the order confirmation page')
def step_impl(context):
    context.f_order_confirmation_page.go_to('checkout-complete.html')


@When('I check the message Checkout: Complete!')
def step_impl(context):
    assert context.f_order_confirmation_page.checkout_verification() == 'Checkout: Complete!'


@When('I click on the left top corner menu(3 horizontal stripes)')
def step_impl(context):
    context.f_order_confirmation_page.menu_click()


@When('I click the logout button')
def step_impl(context):
    context.f_order_confirmation_page.logout_button()


@Then('I check the logout confirmation - Accepted usernames are:')
def step_impl(context):
    context.f_order_confirmation_page.logout_confirmation()
