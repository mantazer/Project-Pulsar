from db import MongoDB
from flask import Flask, request, Response
from model import Beacon
import json
import pdb
import threading
import time

app = Flask(__name__)
mongodb = MongoDB()

thread = threading.Thread(target=mongodb.find_outdated)
thread.start()

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
    payload = request.form
    h_address = payload.get('h_address')
    mongodb.beacon_collection.update({'h_address': h_address}, {'$set': {'last_pulse': time.time()}}, upsert = False)
    return '{}'

@app.route('/powerreply', methods=['POST'])
def parse_reply():
    payload = request.form
    print 'Power Outage: ' + payload.get('powerOutage')
    print 'Corresponding Beacon: ' + payload.get('twilioNumber')
    return '{}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

