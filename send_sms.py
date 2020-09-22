# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC5ca388661f220c59aede71464b7b22a8'
auth_token = 'dfc895772065466686f143de6fa9bfdb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Siddharth The king of world",
                     from_='+12184525296',
                     to='+19799857341'
                 )

print(message.sid)



"""
import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'T0DLLISYKZ11ZQSE7REL3AW989VO0SQ7',
  'secret':'D603ZH98CXK08R7T',
  'usetype':'Stage',
  'phone': 8763511639,
  'message':'Hello,How are you?',
  'senderid':'siddharth'
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest('https://www.sms4india.com/api/v1/sendCampaign', 'T0DLLISYKZ11ZQSE7REL3AW989VO0SQ7', 'D603ZH98CXK08R7T', 'stage', '8763511639', 'siddharth', 'Hello,How are you?' )


# print response if you want
print(response.text)
"""




