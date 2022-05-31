from common import common_methods
from behave import *
from datetime import datetime

@when('we retrieve open orders')
def step_impl(context):
    response = common_methods.get_open_orders()
    context.open_orders = response.json()
    assert not context.open_orders['error']

@then('"{orders_number}" open orders exists!')
def step_impl(context, orders_number):
    assert int(orders_number) == len(context.open_orders['result']['open'])
