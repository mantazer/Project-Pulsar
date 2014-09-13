from twilio.rest import TwilioRestClient
 
# CHANGE THIS FROM TEST
account_sid = "ACe36f8844f05de80021faa460764b6d33"
auth_token  = "f22d67391209d2a4f8f54266cd721978"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+15712589774",    # Replace with your phone number
    from_="+15033964667") # Replace with your Twilio number
print message.sid

#15033964667