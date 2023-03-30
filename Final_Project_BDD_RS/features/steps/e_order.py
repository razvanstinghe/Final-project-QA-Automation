from behave import *


@Given('I am on the order page')
def step_impl(context):
    context.e_order_page.go_to('checkout-step-two.html')


@When('I check the item1 existence in the cart')
def step_impl(context):
    assert context.e_order_page.item1_check() == 'Sauce Labs Backpack'


@When('I check the item4 existence in the cart')
def step_impl(context):
    assert context.e_order_page.item4_check() == 'Sauce Labs Bike Light'


@When('I press the Finish button')
def step_impl(context):
    context.e_order_page.finish_button()


@Then('I check the confirmation message: Checkout: Complete!')
def step_impl(context):
    context.e_order_page.confirmation_message()
