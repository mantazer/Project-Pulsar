from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random
import urllib2
import pdb
import json
import requests
import sendgrid
from sendgrid import SendGridClient, Mail
import simplejson
 
app = Flask(__name__)

SendGridUserName = "b-ball225"
SendGridPassword = "Basketball1"
FromEmail = "inbound@b-ball225.bymail.in"
emailValue = ""
personalNumber = ""
number = ""
numberTwo = ""


@app.route("/SendRequest", methods=['GET', 'POST'])
def start_process():
	global emailValue
	global personalNumber
	global number

	account_sid = "ACe36f8844f05de80021faa460764b6d33"
	auth_token  = "f22d67391209d2a4f8f54266cd721978"
	client = TwilioRestClient(account_sid, auth_token)

	emailValue = request.form['e_address']
	address = request.form['h_address']
	number = request.form['twilio_phone']
	personalNumber = request.form['personal_phone']


	message = client.messages.create(body="OUT",
		to="+14342008920",    # Replace with your phone number
		from_=str(number)) # Replace with your Twilio number
	 
	# message = client.messages.create(body="OUT",
	#     to="+14342008920",    # Replace with your phone number
	#     from_="+15033964667") # Replace with your Twilio number

	#print message.sid
	return "Hello World"

@app.route("/ISPFault", methods=['GET', 'POST'])
def test_bench_ISP():
	account_sid = "ACe36f8844f05de80021faa460764b6d33"
	auth_token  = "f22d67391209d2a4f8f54266cd721978"
	client = TwilioRestClient(account_sid, auth_token)

	resp = twilio.twiml.Response()
	fromValue = request.form['From']
	bodyValue = request.form['Body']
	toValue = request.form['To']

	#print bodyValue

	if(str(bodyValue) == "OUT"):
		outOrNot = random.randint(0,9)
		if(outOrNot <= 4):
			resp.message("An outage was reported in your area. We expect this to be resolved by 6pm today.")

			# message = client.messages.create(body="An outage was reported in your area. We expect this to be resolved by 6pm today.",
			# to=str(personalNumber),    # Replace with your phone number
			# from_=str(number)) # Replace with your Twilio number
		else:
			resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
			# message = client.messages.create(body="An outage was reported in your area. We expect this to be resolved by 6pm today.",
			# to=str(personalNumber),    # Replace with your phone number
			# from_=str(number)) # Replace with your Twilio number
	else:
		resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
		# message = client.messages.create(body="An outage was reported in your area. We expect this to be resolved by 6pm today.",
		# to=str(personalNumber),    # Replace with your phone number
		# from_=str(number)) # Replace with your Twilio number
	print str(resp)
	#print "ISP Fault Done"
	return str(resp)

@app.route("/RecieveResult", methods=['GET', 'POST'])
def recieve_result():
	global numberTwo
	# pdb.set_trace()
	fromValue = request.form['From']
	bodyValue = request.form['Body']
	toValue = request.form['To']
	# print "Body: " + bodyValue
	# print "From: " + fromValue
	# print "To: " + toValue

	value = "True"

	if(str(bodyValue) == "An outage was reported in your area. We expect this to be resolved by 6pm today."):
		value = "False"

	if(value):
		htmlForEmail = '<html><body><img src=\"http://wedte.com/wp-content/uploads/2013/01/PowerOutage.jpg\" alt=\"Power Outage\"><p></p><p></p><h3> We think that your house may have a power outage. If this is true, simply reply to this e-mail with any response so that the Electricty Supplier can serve you faster. <p></p><br><br></h3></body></html>'
		sg = SendGridClient(SendGridUserName, SendGridPassword)

		message = Mail()
		#message.add_to('Gautam <raju@email.virginia.edu>')
		message.add_to(emailValue)
		message.set_subject('Is there a Power Outage at your house?')
		message.set_html(htmlForEmail)
		message.set_from(FromEmail)
		status, msg = sg.send(message)

	payload = {'powerOutage': value, 'twilioNumber': number}
	#pdb.set_trace()
	r = requests.post("http://ec2-54-68-73-74.us-west-2.compute.amazonaws.com:5000/powerreply", data=payload)

	numberTwo = number

	print str(value)
	print numberTwo

	return "Test"

@app.route("/powerreply", methods=['GET', 'POST'])
def show_result():
	powerOutage = request.form['powerOutage']

	# if(ispOutage):
	# 	print "This is working"
	# else:
	# 	print "This is working (2)"

	print "Outage: " + str(powerOutage)

	return str(powerOutage)

#For Sendgrid
@app.route("/inbound", methods=['POST'])
def sendgrid():

	# Consume the entire email
	envelope = simplejson.loads(request.form.get('envelope'))

	# Get some header information
	to_address = envelope['to'][0]
	from_address = envelope['from']
	#text = envelope['text']

	print to_address
	print from_address
	
	#print text

	value = "True"

	payloads = {'powerOutage': value, 'twilioNumber': numberTwo}
	ra = requests.post("http://ec2-54-68-73-74.us-west-2.compute.amazonaws.com:5000/powerreply", data=payloads)

	return "HTTP/1.1 200 OK"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, debug=True)