from model import Beacon
import requests
import time

PROTOCOL = 'http'
HOST = 'ec2-54-68-73-74.us-west-2.compute.amazonaws.com'
PORT = 5000

REGISTER_ENDPOINT = '/register'
LISTEN_ENDPOINT = '/listen'

REGISTER_URL = PROTOCOL + '://' + HOST + ':' + str(PORT) + REGISTER_ENDPOINT
LISTEN_URL = PROTOCOL + '://' + HOST + ':' + str(PORT) + LISTEN_ENDPOINT


def prompt():
    h_address = raw_input('Enter home address (Street address, City, State Zip): ')
    e_address = raw_input('Enter email address: ')
    twilio_phone = 0
    personal_phone = raw_input('Enter personal phone number: ')
    last_pulse = time.time()
    is_dead = 0
    return Beacon(h_address, e_address, twilio_phone, personal_phone, last_pulse, is_dead)

def register(beacon):
    payload = Beacon.jsonify_beacon(beacon)
    r = requests.post(REGISTER_URL, data=payload)
    
    if r.ok:
        print 'Registration successful!'
    else:
        print "Registration failed"

def pulse(beacon):
    while True:
        payload = Beacon.jsonify_beacon(beacon)
        r = requests.post(LISTEN_URL, data=payload)
        time.sleep(2)

def run():
    b = prompt()
    register(b)
    pulse(b)

if __name__ == '__main__':
    run()

