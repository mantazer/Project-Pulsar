__author__ = 'muntaserahmed'

#TODO: create address model
#TODO: check input format

class Beacon:
    def __init__(self, h_address, e_address, phone):
        self.h_address = h_address
        self.e_address = e_address
        self.phone = '+15033964667' # testing purposes

    def jsonify_beacon(self):
        payload = {'address': self.h_address, 'emailAddress': self.e_address, 'phoneNumber': self.phone}
        return payload

