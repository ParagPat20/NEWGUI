import eel
import sys
import os
from functions import send, MCU_host, json_data

# Initialize eel with your web files directory
eel.init('web')

@eel.expose
def login(username, password):
    if username == "parag" and password == "oxitech":
        return True
    return False

@eel.expose
def connect_drone(drone):
    if drone == 'MCU':
        send(MCU_host, 'initialize_MCU()')
        json_data["mcuconnected"] = True
        json_data["connected_devices"] += 1
    return True

if __name__ == '__main__':
    # Start the application
    eel.start('index.html', size=(1500, 760)) 