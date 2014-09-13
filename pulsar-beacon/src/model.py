__author__ = 'muntaserahmed'

class Beacon:
    def __init__(self, h_address, e_address, twilio_phone, personal_phone, last_pulse, is_dead):
        self.h_address = h_address
        self.e_address = e_address
        self.twilio_phone = '+15033964667' # testing purposes
        self.personal_phone = personal_phone
        self.last_pulse = last_pulse
        self.is_dead = is_dead

    def jsonify_beacon(self):
        payload = {'h_address': self.h_address, 'e_address': self.e_address, 'twilio_phone': self.twilio_phone, 'personal_phone': self.personal_phone, 'last_pulse': str(self.last_pulse), 'is_dead': str(self.is_dead)}
        return payload
