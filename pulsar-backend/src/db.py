from pymongo import MongoClient
import requests
import time

PROTOCOL = 'http'
HOST = 'ec2-54-164-3-245.compute-1.amazonaws.com'
PORT = 5000

SEND_REQUEST_ENDPOINT = '/SendRequest'

SEND_REQUEST_URL = PROTOCOL + '://' + HOST + ':' + str(PORT) + SEND_REQUEST_ENDPOINT

class MongoDB:
    client = MongoClient('localhost', 27017)
    db = client.db
    beacon_collection = db.beacon_collection

    def add_if_not_exists(self, beacon):
        if self.beacon_collection.find_one({'h_address': beacon.h_address}) is None:
            beacon_data = {'h_address': beacon.h_address, 'e_address': beacon.e_address, 'twilio_phone': beacon.twilio_phone, 'personal_phone': beacon.personal_phone, 'last_pulse': beacon.last_pulse, 'is_dead': beacon.is_dead}
            beacon_id = self.beacon_collection.insert(beacon_data)
            return beacon_id
        else:
            return None


    def find_outdated(self):
        while True:
            beacons = self.beacon_collection.find()
            for beacon in beacons:
                h_address = beacon.get('h_address')
                e_address = beacon.get('e_address')
                twilio_phone = beacon.get('twilio_phone')
                personal_phone = beacon.get('personal_phone')
                last_pulse = beacon.get('last_pulse')
                is_dead = int(beacon.get('is_dead'))
                if time.time() - float(last_pulse) > 5:
                    if is_dead == 0:
                        print 'DEAD BEACON AT ' + beacon.get('h_address')
                        self.beacon_collection.update({'h_address': h_address}, {'$set': {'is_dead': 1}}, upsert = False)
                        payload = {'h_address': h_address, 'e_address': e_address, 'twilio_phone': twilio_phone, 'personal_phone': personal_phone}
                        print "Pulsing..."
                        r = requests.post(SEND_REQUEST_URL, data=payload)

                        if r.ok:
                            print 'ISP API notified'
                        else:
                            print 'Unable to notify ISP API'

                        return
            time.sleep(5)


