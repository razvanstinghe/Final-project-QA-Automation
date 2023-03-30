from behave import *


@Given('I am on the costumer details page')
def step_impl(context):
    context.d_costumer_page.go_to('checkout-step-one.html')


@When('I leave the First Name1 field empty')
def step_impl(context):
    first_name = ''
    context.d_costumer_page.first_name_1(first_name)


@When('I leave the Last Name1 field empty')
def step_impl(context):
    last_name = ''
    context.d_costumer_page.last_name_1(last_name)


@When('I leave the Zip-Postal Code1 field empty')
def step_impl(context):
    zip_code = ''
    context.d_costumer_page.zip_code_1(zip_code)


@When('I press the Continue button_1')
def step_impl(context):
    context.d_costumer_page.continue_button_1()


@Then('I check the confirmation message_1: Error: First Name is required')
def step_impl(context):
    context.d_costumer_page.confirmation_message_1()


@When('I fill-in the First Name2 field, in letters')
def step_impl(context):
    first_name = 'Razvan'
    context.d_costumer_page.first_name_2(first_name)


@When('I leave the Last Name2 field empty')
def step_impl(context):
    last_name = ''
    context.d_costumer_page.last_name_2(last_name)


@When('I leave the Zip-Postal Code2 field empty')
def step_impl(context):
    zip_code = ''
    context.d_costumer_page.zip_code_2(zip_code)


@When('I press the Continue button_2')
def step_impl(context):
    context.d_costumer_page.continue_button_2()


@Then('I check the confirmation message_2: Error: Last Name is required')
def step_impl(context):
    context.d_costumer_page.confirmation_message_2()


@When('I fill-in the First Name3 field, in letters')
def step_impl(context):
    first_name = 'Razvan'
    context.d_costumer_page.first_name_3(first_name)


@When('I fill-in the Last Name3 field, in letters')
def step_impl(context):
    last_name = 'Stinghe'
    context.d_costumer_page.last_name_3(last_name)


@When('I leave the Zip-Postal Code3 field empty')
def step_impl(context):
    zip_code = ''
    context.d_costumer_page.zip_code_3(zip_code)


@When('I press the Continue button_3')
def step_impl(context):
    context.d_costumer_page.continue_button_3()


@Then('I check the confirmation message_3: Error: Postal Code is required')
def step_impl(context):
    context.d_costumer_page.confirmation_message_3()


@When('I fill-in the First Name4, in digits')
def step_impl(context):
    first_name = '123456'
    context.d_costumer_page.first_name_4(first_name)


@When('I fill-in the Last Name4, in digits')
def step_impl(context):
    last_name = '654321'
    context.d_costumer_page.last_name_4(last_name)


@When('I fill-in the Zip-Postal Code4, in letters')
def step_impl(context):
    zip_code = 'Razvan'
    context.d_costumer_page.zip_code_4(zip_code)


@When('I press the Continue button_4')
def step_impl(context):
    context.d_costumer_page.continue_button_4()


@Then('I check the confirmation message_4: Checkout: Overview')
def step_impl(context):
    context.d_costumer_page.confirmation_message_4()


@When('I fill-in the First Name5, in letters')
def step_impl(context):
    first_name = 'Razvan'
    context.d_costumer_page.first_name_5(first_name)


@When('I fill-in the Last Name5, in letters')
def step_impl(context):
    last_name = 'Stinghe'
    context.d_costumer_page.last_name_5(last_name)


@When('I fill-in the Zip-Postal Code5, in digits')
def step_impl(context):
    zip_code = '123456'
    context.d_costumer_page.zip_code_5(zip_code)


@When('I press the Continue button_5')
def step_impl(context):
    context.d_costumer_page.continue_button_5()


@Then('I check the confirmation message_5: Checkout: Overview')
def step_impl(context):
    context.d_costumer_page.confirmation_message_5()
