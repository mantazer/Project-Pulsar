__author__ = 'muntaserahmed'

class Beacon:
    def __init__(self, h_address, e_address, phone):
        self.h_address = h_address
        self.e_address = e_address
        self.phone = '+15033964667' # testing purposes

    def jsonify_beacon(self):
        payload = {'address': self.h_address, 'emailAddress': self.e_address, 'phoneNumber': self.phone}
        return payload
    
def prompt():
    h_address = raw_input('Enter home address (Street address, City, State Zip: ')
    e_address = raw_input('Enter email address: ')
    phone = raw_input('Enter phone number (+1##########): ')
    return Beacon(h_address, e_address, phone)

