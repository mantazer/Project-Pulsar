from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

@app.route("/ISPFault", methods=['GET', 'POST'])
def test_bench_ISP():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    testing = response.data
    print testing
    # resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
    resp.message(str("testing"))
    return str(resp)

# @app.route("/NotISPFault", methods=['GET', 'POST'])
# def test_bench_ISP():
#     """Respond to incoming calls with a simple text message."""
 
#     resp = twilio.twiml.Response()
#     resp.message("An outage was reported in your area. We expect this to be resolved by 6pm today.")
#     return str(resp)

def sendTwilioSMS():
	# CHANGE THIS FROM TEST
	account_sid = "ACe36f8844f05de80021faa460764b6d33"
	auth_token  = "f22d67391209d2a4f8f54266cd721978"
	client = TwilioRestClient(account_sid, auth_token)
	 
	message = client.messages.create(body="OUT",
	    to="266278",    # Replace with your phone number
	    from_="+15033964667") # Replace with your Twilio number
	print message.sid
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")