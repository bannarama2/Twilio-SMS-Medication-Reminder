#import twilio and other dependencies
import time
from twilio.rest import Client

#hold the SID and the Auth Token for my account
Account_SID = "Axxxxxxxxxxxxxxxxxxxxxxxxx"
Auth_Token = "7zzzzzzzzzzzzzzzzzzzzzzzzzzzz"

client = Client(Account_SID, Auth_Token)

#make the message object
msg = "Take your Feburic Dosage today"

#create the message to send to my phone number using the twilio phone number
while True:
    client.messages.create (to = "YOUR_PHONE_NUMBER", from_ = "PHONE_NUMBER_PROVIDED_BY_TWILIO", body=msg)

    #makes sure that 2 days pass before it resends the message. so 48 hours pass instead of 24 hours. So not daily. But day on and off
    time.sleep(172800)