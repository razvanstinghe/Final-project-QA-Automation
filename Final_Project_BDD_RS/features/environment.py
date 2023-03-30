from features.pages.a_login_page import Login
from features.pages.b_items_page import Select
from features.pages.c_cart_page import Cart
from features.pages.d_customer_page import CostumerDetails
from features.pages.e_order_page import OrderPage
from features.pages.f_logging_out_page import OrderConfirmation
import unittest
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.login_page = Login(context.browser)
    context.items_page = Select(context.browser)
    context.c_cart_page = Cart(context.browser)
    context.d_costumer_page = CostumerDetails(context.browser)
    context.e_order_page = OrderPage(context.browser)
    context.f_order_confirmation_page = OrderConfirmation(context.browser)


def after_all(context):
    context.browser.close()
