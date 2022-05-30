import common_methods as common
from behave import *
from datetime import datetime

@given('API is accessible')
def step_impl(context):
    assert "online" in common.get_system_status()

@when('we get server time')
def step_impl(context):
    context.time = common.get_server_time()
    assert 'rfc1123' in context.time['result']

@when('we retrieve "{pairs}" trading pair')
def step_impl(context, pairs):
    context.pairs_info = common.get_asset_pair(pairs)

@then('server time is correct!')
def step_impl(context):
    datetime_object = datetime.strptime(context.time['result']['rfc1123'], '%a, %d %b %y %H:%M:%S %z')
    today_datetime = datetime.now().date()
    assert datetime_object.date() == today_datetime

@then('"{pairs}" info is available!')
def step_impl(context, pairs):
    assert context.pairs_info['result'][pairs]
    