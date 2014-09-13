from db import MongoDB
from flask import Flask, request, Response
from model import Beacon
import json
import pdb
import threading

app = Flask(__name__)
mongodb = MongoDB()

@app.route('/')
def index():
    return 'working'

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        payload = request.form
         
        h_address = payload.get('h_address')
        e_address = payload.get('e_address')
        twilio_phone = payload.get('twilio_phone')
        personal_phone = payload.get('personal_phone')
        last_pulse = payload.get('last_pulse')
        is_dead = payload.get('is_dead')
        
        b = Beacon(h_address, e_address, twilio_phone, personal_phone, last_pulse, is_dead)
        beacon_id = mongodb.add_if_not_exists(b)

        if beacon_id is not None:
            return Response(response=json.dumps({}), status=201)
        print 'db insertion failed'
        return Response(response=json.dumps({}), status=500)

@app.route('/listen', methods=['POST'])
def listen():
    # TODO: Scale this via threading
    # hit /SendRequest
    t = threading.Thread(target=mongodb.find_outdated, 1)
    t.start()
    return 'listening...'

@app.route('/powerreply', methods=['POST'])
def parse_reply():
    payload = request.form
    print payload.get('powerOutage')
    print payload.get('twilioNumber')
    return 'hi'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

