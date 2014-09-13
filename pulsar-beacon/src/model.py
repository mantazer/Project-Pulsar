__author__ = 'muntaserahmed'

#TODO: create address model
#TODO: check input format

class Beacon:
    def __init__(self, h_address, e_address, phone):
        self.h_address = h_address
        self.e_address = e_address
        self.phone = '+15033964667' # testing purposes

    def jsonify_beacon(self):
        payload = {'h_address': self.h_address, 'e_address': self.e_address, 'phone': self.phone}
        return payload
    
def prompt():
    h_address = raw_input('Enter home address (ex: 123 1st Street, Charlottesville, VA 22903): ')
    e_address = raw_input('Enter email address: ')
    phone = raw_input('Enter phone number (ex: +14341234567): ')
    return Beacon(h_address, e_address, phone)

