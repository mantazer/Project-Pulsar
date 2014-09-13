from pymongo import MongoClient
import time

class MongoDB:
    client = MongoClient('localhost', 27017)
    db = client.db
    beacon_collection = db.beacon_collection

    def add_if_not_exists(self, beacon):
        if self.beacon_collection.find_one({'h_address': beacon.h_address}) is None:
            beacon_data = {'h_address': beacon.h_address, 'e_address': beacon.e_address, 'twilio_phone': beacon.twilio_phone, 'personal_phone': beacon.personal_phone, 'last_pulse': beacon.last_pulse, 'is_dead': beacon.is_dead}
            beacon_id = self.beacon_collection.insert(beacon_data)
            return beacon_id

    def find_outdated(self, i):
        while True:
            print i
            time.sleep(1)


