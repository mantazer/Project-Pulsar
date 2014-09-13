from model import Beacon, prompt
import requests

PROTOCOL = 'http'
HOST = 'ec2-54-68-73-74.us-west-2.compute.amazonaws.com'
PORT = 5000

REGISTER_ENDPOINT = '/register'

REGISTER_URL = PROTOCOL + '://' + HOST + ':' + str(PORT) + REGISTER_ENDPOINT


def register():
    b = prompt()
    payload = Beacon.jsonify_beacon(b)
    r = requests.post(REGISTER_URL, data=payload)

def pulse():
    return 'pulse'

def run():
    register_prompt()
    pulse() 

if __name__ == '__main__':
    register()

