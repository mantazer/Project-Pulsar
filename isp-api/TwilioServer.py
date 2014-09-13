from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random
import urllib2
import pdb
import json
import requests
import sendgrid
import simplejson
 
app = Flask(__name__)

SendGridUserName = "b-ball225"
SendGridPassword = "Basketball1"
FromEmail = "inbound@b-ball225.bymail.in"


@app.route("/SendRequest", methods=['GET', 'POST'])
def start_process():
	account_sid = "ACe36f8844f05de80021faa460764b6d33"
	auth_token  = "f22d67391209d2a4f8f54266cd721978"
	client = TwilioRestClient(account_sid, auth_token)

	# email = request.form['e_address']
 #    address = request.form['h_address']
 #    number = request.form['phone']

	# message = client.messages.create(body="OUT",
	#     to="+14342008920",    # Replace with your phone number
	#     from_=str(number)) # Replace with your Twilio number
	 
	message = client.messages.create(body="OUT",
	    to="+14342008920",    # Replace with your phone number
	    from_="+15033964667") # Replace with your Twilio number

	#sending e-mail
	htmlForEmail = '<html><body><img src=\"http://wedte.com/wp-content/uploads/2013/01/PowerOutage.jpg\" alt=\"Power Outage\"><p></p><p></p><h3> We think that your house may have a power outage. If this is true, simply reply to this e-mail with any response so that the Electricty Supplier can serve you faster. <p></p><br><br></h3></body></html>'
	#sg = sendgrid.SendGridClient(SendGridUserName, SendGridPassword)

	message = sendgrid.Mail()
	message.add_to('Gautam <raju@email.virginia.edu>')
	# message.add_to(email)
	message.set_subject('Is there a Power Outage at your house?')
	message.set_html(htmlForEmail)
	message.set_from(FromEmail)
	#status, msg = sg.send(message)

	#print message.sid
	return "Hello World"

@app.route("/ISPFault", methods=['GET', 'POST'])
def test_bench_ISP():
    resp = twilio.twiml.Response()
    fromValue = request.form['From']
    bodyValue = request.form['Body']
    toValue = request.form['To']

    #print bodyValue

    if(str(bodyValue) == "OUT"):
    	outOrNot = random.randint(0,9)
    	if(outOrNot <= 4):
    		resp.message("An outage was reported in your area. We expect this to be resolved by 6pm today.")
    	else:
    		resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
    else:
    	resp.message("We are not currently aware of a service outage in your area. If you are having trouble with your service, please call 1-800-COMCAST.")
    #print str(resp)
    #print "ISP Fault Done"
    return str(resp)

@app.route("/RecieveResult", methods=['GET', 'POST'])
def recieve_result():
	# pdb.set_trace()
	fromValue = request.form['From']
	bodyValue = request.form['Body']
	toValue = request.form['To']
	# print "Body: " + bodyValue
	# print "From: " + fromValue
	# print "To: " + toValue

	value = "False"

	if(str(bodyValue) == "An outage was reported in your area. We expect this to be resolved by 6pm today."):
		value = "True"

	payload = {'ispOutage': value}
	#pdb.set_trace()
	r = requests.post("http://ec2-54-164-3-245.compute-1.amazonaws.com:5000/isp_reply", data=payload)

	return "Test"

@app.route("/isp_reply", methods=['GET', 'POST'])
def show_result():
    resp = twilio.twiml.Response()
    ispOutage = request.form['ispOutage']

    # if(ispOutage):
    # 	print "This is working"
    # else:
    # 	print "This is working (2)"

    print "Outage: " + str(ispOutage)

    return str(ispOutage)

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

	payload = {'ispOutage': value}
	r = requests.post("http://ec2-54-164-3-245.compute-1.amazonaws.com:5000/isp_reply", data=payload)

	return "HTTP/1.1 200 OK"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)