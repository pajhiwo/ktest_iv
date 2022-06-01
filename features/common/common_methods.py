import os
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64

API_URL = os.environ['API_URL']
API_KEY = os.environ['API_KEY']
API_SEC = os.environ['API_SEC']
PASS_2FA = os.environ['PASS_2FA']

def get_system_status() -> requests.models.Response:
    response = requests.get(f'{API_URL}/0/public/SystemStatus')
    return response

def get_server_time() -> requests.models.Response:
    response = requests.get(f'{API_URL}/0/public/Time')
    return response

def get_asset_pair(pairs) -> requests.models.Response:
    response = requests.get(f'{API_URL}/0/public/AssetPairs?pair={pairs}')
    return response

def get_k_signature(urlpath:str, data: str, secret:str) -> str:
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def k_request(uri_path: str, data: str, API_KEY: str, API_SEC: str) -> requests.models.Response:
    headers = {}
    headers['API-Key'] = API_KEY
    headers['API-Sign'] = get_k_signature(uri_path, data, API_SEC)             
    req = requests.post((API_URL + uri_path), headers=headers, data=data)
    return req

def get_open_orders() -> requests.models.Response:
    response = k_request('/0/private/OpenOrders', {
        "nonce": str(int(1000*time.time())),
        "otp": PASS_2FA,
        "trades": True
    }, API_KEY, API_SEC)

    return response
