from db import MongoDB
from flask import Flask, request, Response
from model import Beacon
import json
import pdb

app = Flask(__name__)
mongodb = MongoDB()

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        payload = request.form
        #TODO: make sure all data comes in
         
        h_address = payload.get('h_address')
        e_address = payload.get('e_address')
        phone = payload.get('phone')
        
        b = Beacon(h_address, e_address, phone)
        beacon_id = mongodb.add_if_not_exists(b)

        if beacon_id is not None:
            return Response(response=json.dumps({}), status=201)
        print 'db insertion failed'
        return Response(response=json.dumps({}), status=500)

@app.route('/listen')
def listen():
    # hit /SendRequest
    # respone key ispOutage
    return 'listening...'

@app.route('/ispreply')
def parse_reply():
    payload = request.form
    print payload.get('ispOutage')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

