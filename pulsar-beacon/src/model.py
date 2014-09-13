__author__ = 'muntaserahmed'

class Beacon:
    def __init__(self, h_address, e_address, phone):
        self.h_address = h_address
        self.e_address = e_address
        self.phone = '+15033964667' # testing purposes

    def jsonify_beacon(self):
        payload = {'address': h_address, 'emailAddress': e_address, 'phoneNumber': phone}
        return payload
    
def prompt():
    h_address = raw_input('Enter home address (Street Address, City, State Zip: ')
    e_address = raw_input('Enter email address: ')
    phone = raw_input('Enter phone number (+1XXXXXXXXXX): ')
    return Beacon(h_address, e_address, phone)

