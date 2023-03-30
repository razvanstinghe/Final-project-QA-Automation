from behave import *


@Given('I am on the shopping cart page')
def step_impl(context):
    context.c_cart_page.go_to('cart.html')


@When('I press the Remove button for the 5th item-Sauce Labs Fleece Jacket')
def step_impl(context):
    context.c_cart_page.remove_item4()


@When('I press the Checkout button')
def step_impl(context):
    context.c_cart_page.checkout_button()


@Then('I check the confirmation message: Checkout: Your Information')
def step_impl(context):
    context.c_cart_page.confirmation_message()
