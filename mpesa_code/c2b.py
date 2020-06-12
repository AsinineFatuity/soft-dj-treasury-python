import requests
from requests.auth import HTTPBasicAuth

from access_token import generate_access_token
import keys 

def register_url ():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = { 
      "ShortCode": keys.c2b_short_code,
      "ResponseType": "Completed",
      "ConfirmationURL": "https://asininefatuity.com/confirmation",
      "ValidationURL": "https://asininefatuity.com/validation_url"}
  
    response = requests.post(api_url, json = request, headers=headers)
  
    print (response.text)

#register_url() run it only once to register urls with safaricom servers
def simulate_transaction_c2b ():
        my_access_token = generate_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        headers = {"Authorization": "Bearer %s" % my_access_token}
        request = { 
        "ShortCode":keys.c2b_short_code,
        "CommandID":"CustomerPayBillOnline", # can be this or buy goods online
        "Amount":"2",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber":"35842347" #can be invoice/ id number etc, will be used in future for validation
        }

        response = requests.post(api_url, json = request, headers=headers)

        print (response.text)
simulate_transaction_c2b()

  
  