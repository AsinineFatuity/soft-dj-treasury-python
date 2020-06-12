import requests
from requests.auth import HTTPBasicAuth


from access_token import generate_access_token
from enco_deco import generate_password
import keys
from utils import get_timestamp


def Lipa_na_mpesa ():
    my_formatted_time = get_timestamp()
    my_password = generate_password(my_formatted_time) 
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.business_short_code,
    "Password": my_password,
    "Timestamp": my_formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": keys.phone_number,
    "PartyB": keys.business_short_code,
    "PhoneNumber": keys.phone_number ,
    "CallBackURL": "https://asininefatuity.com",
    "AccountReference": "f17/81870/2017 ",
    "TransactionDesc": "pay compliments"
    }
    response = requests.post(api_url, json = request, headers=headers)
    print (response.text)
Lipa_na_mpesa ()