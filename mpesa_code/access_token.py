import requests
from requests.auth import HTTPBasicAuth
import keys


def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json() #'access_token': 'xxxxxxx', 'expires_in': '3599'
    access_token_extract = json_response ['access_token']#extract the value from the dict's key-value pair
    
    return access_token_extract