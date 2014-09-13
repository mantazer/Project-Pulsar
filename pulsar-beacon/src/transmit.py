from model import Beacon
import requests

PROTOCOL = 'http'
HOST = 'ec2-54-68-73-74.us-west-2.compute.amazonaws.com'
PORT = 5000

REGISTER_ENDPOINT = '/register'

REGISTER_URL = PROTOCOL + '://' + HOST + ':' + str(PORT) + REGISTER_ENDPOINT


def prompt():
    h_address = raw_input('Enter home address (Street address, City, State Zip: ')
    e_address = raw_input('Enter email address: ')
    twilio_phone = raw_input('Enter provided twilio phone number (+1##########): ')
    personal_phone = raw_input('Enter personal phone number: (+1##########): ')
    return Beacon(h_address, e_address, twilio_phone, personal_phone)

def register(beacon):
    payload = Beacon.jsonify_beacon(beacon)
    r = requests.post(REGISTER_URL, data=payload)
    
    if r.ok:
        print 'Registration successful!'
    else:
        print "Registration failed"

def pulse():
    pass    

def run():
    b = prompt()
    register(b)

if __name__ == '__main__':
    run()

