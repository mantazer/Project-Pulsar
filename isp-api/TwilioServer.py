from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random
import urllib2
import pdb
import json
 
app = Flask(__name__)


@app.route("/SendRequest", methods=['GET', 'POST'])
def start_process():
	account_sid = "ACe36f8844f05de80021faa460764b6d33"
	auth_token  = "f22d67391209d2a4f8f54266cd721978"
	client = TwilioRestClient(account_sid, auth_token)

	# email = request.form['emailAddress']
 #    address = request.form['address']
 #    number = request.form['phoneNumber']

	# message = client.messages.create(body="OUT",
	#     to="+14342008920",    # Replace with your phone number
	#     from_=str(number)) # Replace with your Twilio number
	 
	message = client.messages.create(body="OUT",
	    to="+14342008920",    # Replace with your phone number
	    from_="+15033964667") # Replace with your Twilio number

	print message.sid
	return "Hello World"

@app.route("/ISPFault", methods=['GET', 'POST'])
def test_bench_ISP():
    resp = twilio.twiml.Response()
    fromValue = request.form['From']
    bodyValue = request.form['Body']
    toValue = request.form['To']

    print bodyValue

    if(str(bodyValue) == "OUT"):
    	outOrNot = random.randint(0,9)
    	if(outOrNot <= 4):
    		resp.message("An outage was reported in your area. We expect this to be resolved by 6pm today.")
    	else:
    		resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
    else:
    	resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
    print str(resp)
    print "ISP Fault Done"
    return str(resp)

@app.route("/RecieveResult", methods=['GET', 'POST'])
def recieve_result():
	# pdb.set_trace()
	fromValue = request.form['From']
	bodyValue = request.form['Body']
	toValue = request.form['To']
	print "Body: " + bodyValue
	print "From: " + fromValue
	print "To: " + toValue

	value = "False"

	if(str(bodyValue) == "An outage was reported in your area. We expect this to be resolved by 6pm today."):
		value = "True"

	payload = json.dumps({'ispOutage': value})

	r = requests.post("http://ec2-54-165-202-14.compute-1.amazonaws.com:5000/isp_reply", payload)

	return "Test"

@app.route("/isp_reply", methods=['GET', 'POST'])
def show_result():
    resp = twilio.twiml.Response()
    ispOutage = request.form['ispOutage']

    if(ispOutage):
    	print "This is working"
    else:
    	print "This is working (2)"

    print "Outage: " + str(ispOutage)

    return str(ispOutage)

#http://ec2-54-165-202-14.compute-1.amazonaws.com:5000/isp_reply
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")