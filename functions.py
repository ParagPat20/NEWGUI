import zmq
import time
import threading
import tkintermapview
import tkinter
import logging

MCU_host = '192.168.54.229'
CD1_host = '192.168.54.101'
CD2_host = '192.168.54.225'
CD3_host = CD2_host
CD4_host = CD1_host
pc = '192.168.54.192'
hosts = {
    'MCU' : MCU_host,
    'CD1' : CD1_host,
    'CD2' : CD2_host,
    'CD3' : CD3_host,
    'CD4' : CD4_host
}
add_marker = None
cmd_port = 12345
ctrl_port = 54321
selected_drone = []
context = zmq.Context()  # Create a ZeroMQ context
poller = zmq.Poller
connected_hosts = set()
clients = {}

coordslat = {
    "MCU" : 22.2868240,
    "CD1" : 22.2868215,
    "CD2" : 22.2867266,
    "CD3" : 22.2867117,
    "CD4" : 22.2867128,
    }
coordslon = {
    "MCU" : 73.3639982,
    "CD1" : 73.3642235,
    "CD2" : 73.3642369,
    "CD3" : 73.3640009,
    "CD4" : 73.3640029
    }
cap = None
mission = ["Edit"]
import random

json_data = {
    "mcuconnected": False,
    "cd1connected": False,
    "cd2connected": False,
    "cd3connected": False,
    "cd4connected": False,
    "cd5connected": False,
    "connected_devices" : 0,
    "armed" : False,
    "mode" : "",
    "camera" : False,
    "claw" : False,
    "control" : False,
    "takeoff" : False,
    "poshold" : False,
    "land" : False,
}

def json_data_reset():
    global json_data
    json_data_res = {
        "mcuconnected": False,
        "cd1connected": False,
        "cd2connected": False,
        "cd3connected": False,
        "cd4connected": False,
        "cd5connected": False,
        "connected_devices" : 0,
    }
    json_data = json_data_res
    logger.log("Database Reset Started")


def send(host, immediate_command_str):
    global connected_hosts
    global clients

    try:
        if host not in connected_hosts:
            connect_and_register_socket(host)
            log_start_message="log_reset_server()"
            clients[host].send(log_start_message.encode(), zmq.NOBLOCK)  # Non-blocking send


            immediate_command_str = str(immediate_command_str)

        clients[host].send(immediate_command_str.encode(), zmq.NOBLOCK)  # Non-blocking send
        logger.log("Command sent successfully to {}".format(host))

    except zmq.error.Again:  # Handle non-blocking send errors
        poller.register(clients[host], zmq.POLLOUT)  # Wait for socket readiness
        socks = dict(poller.poll(1000))
        if clients[host] in socks and socks[clients[host]] == zmq.POLLOUT:
            clients[host].send_string(immediate_command_str)  # Retry sending
        else:
            logger.log("Socket not ready for {}, reconnecting...".format(host))
            reconnect_socket(host)

    except zmq.error.ZMQError as e:
        logger.log("PC Host {host}: {}".format(e))
        reconnect_socket(host)  # Attempt reconnection

def connect_and_register_socket(host):
    socket = context.socket(zmq.PUSH)
    socket.setsockopt(zmq.SNDHWM, 1000)  # Allow up to 1000 queued messages
    socket.connect(f"tcp://{host}:12345")
    clients[host] = socket
    connected_hosts.add(host)
    logger.log("Clients: {}".format(clients))

def reconnect_socket(host):
    socket = clients[host]
    socket.close()
    socket = context.socket(zmq.PUSH)
    socket.connect(f"tcp://{host}:12345")
    clients[host] = socket
    socks = dict(poller.poll(1000))  # Wait for write events with timeout


def recv_status(remote_host,status_port, param=None):
    logger.log("just chilling")
  
set_vel = False
def send_ctrl(cmd):
    global selected_drone
    global set_vel
    if set_vel == True:
        Velocity = 0.6
        set_vel = False
    else:
        Velocity = 0.4
    x = '0'
    y = '0'
    z = '0'
    if cmd == 'w':
        x = str(Velocity)
    elif cmd == 's':
        x = str(-Velocity)
    if cmd == 'a':
        y = str(Velocity)
    elif cmd == 'd':
        y = str(-Velocity)
    if cmd == 'u':
        z = str(-0.2)
    elif cmd == 'j':
        z = str(0.2)

    logger.log("Selected_Drone is : {}".format(selected_drone))
    command(f'send_ned_velocity({x},{y},{z})')
    logger.log("Sending ned velocity to {}\n X={}, Y={}, Z={}".format(selected_drone,x,y,z))

landon=False
mcuon=False
cd1on=False
cd2on=False
cd3on = None
cd4on = None
clawon = None

def toggle_buttons(root,button_name):
    global mcuon,cd1on,cd2on,cd3on,cd4on,landon,clawon
    try:
        if button_name == 'land':
            if landon==False:
                root.landonbtn()
                landon=True
            else:
                root.landoffbtn()
                landon=False
        if button_name == 'mcu':
            if mcuon==False:
                root.mcuonbtn()
                mcuon=True
            else:
                root.mcuoffbtn()
                mcuon=False
        if button_name == 'cd1':
            if cd1on==False:
                root.cd1onbtn()
                cd1on=True
            else:
                root.cd1offbtn()
                cd1on=False

        if button_name == 'cd2':
            if cd2on==False:
                root.cd2onbtn()
                cd2on=True
            else:
                root.cd2offbtn()
                cd2on=False

        if button_name == 'cd3':
            if cd3on==False:
                root.cd3onbtn()
                cd3on=True
            else:
                root.cd3offbtn()
                cd3on=False
        
        if button_name == 'cd4':
            if cd4on==False:
                root.cd4onbtn()
                cd4on=True
            else:
                root.cd4offbtn()
                cd4on=False

        if button_name == 'clawon':
            if clawon==False:
                root.clawonbtn()
                clawon = True
            else:
                root.clawoffbtn2()
                clawon=False
    except Exception as e:
        logger.log(e)


def speedup():
    global set_vel
    set_vel = True
    logger.log("Set_vel = {}".format(set_vel))


def ctrlON(root):

    if root.control_type == 'ctrl_front':
        root.bind('w', lambda event: command("ctrl_front(0.5)"))
        root.bind('a', lambda event: command("ctrl_yaw(-1)"))
        root.bind('d', lambda event: command("ctrl_yaw(1)"))
        root.bind('u', lambda event: send_ctrl('u'))
        root.bind('j', lambda event: send_ctrl('j'))
        root.bind('s', lambda event: command('ctrl_front(-0.5)'))
    if root.control_type == 'send_ned':
        root.bind('u', lambda event: send_ctrl('u'))
        root.bind('j', lambda event: send_ctrl('j'))
        root.bind('w', lambda event: send_ctrl('w'))
        root.bind('s', lambda event: send_ctrl('s'))
        root.bind('a', lambda event: send_ctrl('a'))
        root.bind('d', lambda event: send_ctrl('d'))
        root.bind('h', lambda event: command("ctrl_yaw(-1)"))
        root.bind('k', lambda event: command("ctrl_yaw(1)"))
        root.bind('x', lambda event: speedup())

    root.bind('l', lambda event: toggle_buttons(root,'land'))
    root.bind('1', lambda event: toggle_buttons(root,'mcu'))
    root.bind('2', lambda event: toggle_buttons(root,'cd1'))
    root.bind('3', lambda event: toggle_buttons(root,'cd2'))
    root.bind('4', lambda event: toggle_buttons(root,'cd3'))
    root.bind('5', lambda event: toggle_buttons(root,'cd4'))
    root.bind('c', lambda event: toggle_buttons(root,'clawon'))
    logger.log("Control_type:{}".format(root.control_type))

    logger.log("CONTROL ON {}".format(selected_drone))

def ctrlOFF(root):
    root.unbind('w')
    root.unbind('a')
    root.unbind('d')
    root.unbind('u')
    root.unbind('j')
    root.unbind('s')
    root.unbind('l')
    root.unbind('1')
    root.unbind('2')
    root.unbind('3')
    root.unbind('4')
    root.unbind('5')
    root.unbind('c')
    logger.log("CONTROL OFF")

def select_drone(string,en):
    global selected_drone
    if en == True:
        selected_drone.append(string)
    else:
        if string in selected_drone:
            selected_drone.remove(string)

    logger.log(selected_drone)

def command(cmd):
    global selected_drone
    for drone in selected_drone:
        send(hosts[drone],f"{drone}.{cmd}")

def add_marker1():
    global add_marker
    add_marker.add_given_markers()

class Logger:
    def __init__(self):
        self.log_text = None
        self.log_text_sec = None
        self.mcu_status = False
        self.cd1_status = False
        self.cd2_status = False
        self.log_thread = None
        self.context = zmq.Context()
        socket = self.context.socket(zmq.REP)  # Use self.context consistently
        self.router_socket = self.context.socket(zmq.ROUTER)

    def set_log_text(self, log_text):
        self.log_text = log_text

    def log(self, message):
        if self.log_text:
            self.log_text.configure(state="normal", foreground="#5E95FF")
            message = str(message)
            self.log_text.insert("end", message + "\n")
            self.log_text.configure(state="disabled")
            self.log_text.see("end")

    def set_log_text_sec(self, log_text):
        self.log_text_sec = log_text

    def log_sec(self, message):
        if self.log_text_sec:
            self.log_text_sec.configure(state="normal", foreground="#FF0000")
            message = str(message)
            self.log_text_sec.insert("end", message + "\n")
            self.log_text_sec.configure(state="disabled")
            self.log_text_sec.see("end")

    def start_logging(self):
        try:
            self.log("LOGGING SERVER STARTED!")
            self.log_sec("WAITING FOR SECURITY PARAMS!!!")
            self.log_thread = threading.Thread(target=self.handle_messages)
            self.log_thread.start()
            self.router_socket.bind("tcp://*:5556")

            # Wifi Security Code
            socket = context.socket(zmq.REP)  # REP socket for responding to clients
            socket.bind("tcp://*:8888")  # Bind to port 8888 (matching client configuration)
            while True:
                message = socket.recv()  # Receive request from client
                try:
                    socket.send_string("Connected")  # Send response to client
                except Exception as e:
                    print(f"Error checking Wi-Fi: {e}")
                    socket.send_string("Error")  # Notify client of an error

        except zmq.ZMQError as e:
            logging.error("Error connecting to server: %s", e)

    def handle_messages(self):
        global add_marker
        global coordslat
        global coordslon
        while True:
            try:
                message = self.router_socket.recv_multipart()
                message = message[1].decode()
                message = str(message)
                try:
                    # Process messages appropriately
                    if message.startswith("sec "):
                        self.log_sec(message[4:])

                    elif message.startswith("lat "):
                        parts = message.split()
                        drone_name = parts[1]
                        coordslat[drone_name] = float(parts[2])
                        self.log_sec(coordslat[drone_name])

                    elif message.startswith("lon "):
                        parts = message.split()
                        drone_name = parts[1]
                        coordslon[drone_name] = float(parts[2])
                        self.log_sec(coordslon[drone_name])
                    else:
                        self.log(message)
                except Exception as e:
                    logging.error("Error processing message: %s", e)
            except zmq.ZMQError as e:
                if e.errno != zmq.ETERM:
                    logging.error("Error receiving message: %s", e)

logger = Logger()

def start_logging_in_background():
    logger.start_logging()

class MapApplication():
    def __init__(self, root):
        global coordslat
        global coordslon
        self.coords = []

        self.map_widget = tkintermapview.TkinterMapView(root)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        logger.log_sec(str(self.coords))
        lat = coordslat["MCU"]
        lon = coordslon["MCU"]
        self.map_widget.set_position(lat, lon)
        self.map_widget.set_zoom(30)
        self.add_given_markers()
        self.map_widget.add_right_click_menu_command(label="Add Given Markers",
                                                     command=self.add_given_markers)
        threading.Thread(target=self.infmarker).start()

    def add_given_markers(self):
        self.map_widget.delete_all_marker()

        given_coordinates = [
            {"lat": coordslat["MCU"], "lon": coordslon["MCU"], "label": "MCU"}
        ]
        for data in given_coordinates:
            lat = data["lat"]
            lon = data["lon"]
            label = data["label"]
            # Use individual latitude and longitude values
            self.map_widget.set_marker(lat, lon, text=label)
        self.map_widget.set_position(lat,lon)

    def infmarker(self):
        while True:
            self.add_given_markers()
            time.sleep(3)
