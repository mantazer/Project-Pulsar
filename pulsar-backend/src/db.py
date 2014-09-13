from pymongo import MongoClient

class MongoDB:
    client = MongoClient('localhost', 27017)
    db = client.db
    beacon_collection = db.beacon_collection

    def add_if_not_exists(self, beacon):
        if self.beacon_collection.find_one({'h_address': beacon.h_address}) is None:
            beacon_data = {'h_address': beacon.h_address, 'e_address': beacon.e_address, 'phone': beacon.phone}
            beacon_id = self.beacon_collection.insert(node_data)
            return beacon_id

