from behave import *


@Given('I am on the buying page')
def step_impl(context):
    context.items_page.go_to('inventory.html')


@When('I press the filter drop-down list')
def step_impl(context):
    context.items_page.filter_items_z_a()


@When('I select filtration from Z to A')
def step_impl(context):
    context.items_page.z_a_button()


@Then('I check if item Test.allTheThings() T-Shirt (Red) is the 1st item')
def step_impl(context):
    context.items_page.check_item_z_a()


@When('I press again the filter drop-down list')
def step_impl(context):
    context.items_page.filter_items_a_z()


@When('I select filtration from A to Z')
def step_impl(context):
    context.items_page.a_z_button()


@Then('I check if item Sauce Labs Backpack is the 1st item')
def step_impl(context):
    context.items_page.check_item_a_z()


@When('I press Add to cart button for the 1st item-Sauce Labs Backpack')
def step_impl(context):
    context.items_page.add_item1()


@When('I press Add to cart button for the 2nd item-Sauce Labs Bolt T-Shirt')
def step_impl(context):
    context.items_page.add_item2()


@When('I press Add to cart button for the 4th item-Sauce Labs Bike Light')
def step_impl(context):
    context.items_page.add_item4()


@When('I press the Remove button for the 2nd item-Sauce Labs Bolt T-Shirt')
def step_impl(context):
    context.items_page.remove_item2()


@When('I press Add to cart button for the 5th item-Sauce Labs Fleece Jacket')
def step_impl(context):
    context.items_page.add_item5()


@When('I press the Cart button')
def step_impl(context):
    context.items_page.cart_button()


@Then('I check the confirmation message: Your Cart')
def step_impl(context):
    context.items_page.confirmation_message()
