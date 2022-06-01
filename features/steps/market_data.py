from common import common_methods
from common import const
from behave import *
from datetime import datetime

@given('API is accessible')
def step_impl(context):
    response = common_methods.get_system_status()
    assert "online" in response.json()['result']['status']

@when('we get server time')
def step_impl(context):
    response = common_methods.get_server_time()
    context.time = response.json()
    assert 'rfc1123' in context.time['result']
    assert not context.time['error']
    assert sorted(const.RESPONSE_HEADERS_MARKET_DATA) == sorted(list(response.headers.keys()))

@when('we retrieve "{pairs}" trading pair')
def step_impl(context, pairs):
    response = common_methods.get_asset_pair(pairs)
    context.pairs_info = response.json()
    assert not context.pairs_info['error']
    assert sorted(const.RESPONSE_HEADERS_MARKET_DATA) == sorted(list(response.headers.keys()))

@then('server time is correct!')
def step_impl(context):
    datetime_object = datetime.strptime(context.time['result']['rfc1123'], '%a, %d %b %y %H:%M:%S %z')
    today_datetime = datetime.now().date()
    assert datetime_object.date() == today_datetime

@then('"{pairs}" info is available!')
def step_impl(context, pairs):
    assert context.pairs_info['result'][pairs]
    