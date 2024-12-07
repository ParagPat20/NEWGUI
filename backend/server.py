from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add parent directory to path
from functions import *  # Import your existing functions

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == "parag" and password == "oxitech":
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/connect_drone', methods=['POST'])
def connect_drone():
    data = request.get_json()
    drone = data.get('drone')
    
    if drone == 'MCU':
        send(MCU_host, 'initialize_MCU()')
        json_data["mcuconnected"] = True
        json_data["connected_devices"] += 1
    # Add similar logic for other drones
    
    return jsonify({"success": True})

# Add more endpoints for other functionality

if __name__ == '__main__':
    app.run(port=5000) 