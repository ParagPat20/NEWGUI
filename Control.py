from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from functions import *
import cv2
import numpy as np

p=120

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Control")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def control():
    CTRL()

class CTRL(Frame):
    camera_clients = []

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.ctrlonmcu = False
        self.ctrloncd1 = False
        self.ctrloncd2 = False
        

        self.configure(bg = "#2A282C")

        self.canvas = Canvas(
            self,
            bg = "#2A282C",
            height = 725,
            width = 420,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.overlay_win_active = False

        self.canvas.place(x = 0, y = 0)

        self.canvas.create_text(
            179.0,
            16.0,
            anchor="nw",
            text="Control",
            fill="#FFFFFF",
            font=("CaveatRoman Regular", 24 * -1)
        )

        self.boxmcuim = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.boxmcu = self.canvas.create_image(
            210.0,
            124.0,
            image=self.boxmcuim
        )

        self.canvas.create_text(
            56.0,
            95.0,
            anchor="nw",
            text="MCU",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        self.cammcuim = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.cammacu = self.canvas.create_image(
            31.71429443359375,
            110.0,
            image=self.cammcuim
        )

        self.ctrloffmcuim = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.ctrloffmcucanvas = self.canvas.create_image(
            343.0,
            111.0,
            image=self.ctrloffmcuim
        )

        self.ctrlonmcuim = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.ctrlonmcucanvas = self.canvas.create_image(
            343.0,
            111.0,
            image=self.ctrlonmcuim
        )

        self.accoffmcuim = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.accoffmcucanvas = self.canvas.create_image(
            211.0,
            112.0,
            image=self.accoffmcuim
        )

        self.acconmcuim = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.acconmcucanvas = self.canvas.create_image(
            211.0,
            112.0,
            image=self.acconmcuim
        )

        self.canvas.tag_bind(self.ctrloffmcucanvas, "<Button-1>" , lambda x: self.ctrloffmcu())
        self.canvas.tag_bind(self.ctrlonmcucanvas, "<Button-1>" , lambda x: self.ctrlonmcubtn())
        self.canvas.tag_bind(self.accoffmcucanvas, "<Button-1>" , lambda x: self.accessoffmcu())
        self.canvas.tag_bind(self.acconmcucanvas, "<Button-1>" , lambda x: self.accessmcu())

        self.boxcd1im = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.boxcd1 = self.canvas.create_image(
            210.0,
            124.0+p,
            image=self.boxcd1im
        )

        self.canvas.create_text(
            56.0,
            95.0+p,
            anchor="nw",
            text="CD1",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        self.camcd1im = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.cammacu = self.canvas.create_image(
            31.71429443359375,
            110.0+p,
            image=self.camcd1im
        )

        self.ctrloffcd1im = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.ctrloffcd1canvas = self.canvas.create_image(
            343.0,
            111.0+p,
            image=self.ctrloffcd1im
        )

        self.ctrloncd1im = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.ctrloncd1canvas = self.canvas.create_image(
            343.0,
            111.0+p,
            image=self.ctrloncd1im
        )

        self.accoffcd1im = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.accoffcd1canvas = self.canvas.create_image(
            211.0,
            112.0+p,
            image=self.accoffcd1im
        )

        self.acconcd1im = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.acconcd1canvas = self.canvas.create_image(
            211.0,
            112.0+p,
            image=self.acconcd1im
        )

        self.canvas.tag_bind(self.ctrloffcd1canvas, "<Button-1>" , lambda x: self.ctrloffcd1())
        self.canvas.tag_bind(self.ctrloncd1canvas, "<Button-1>" , lambda x: self.ctrloncd1btn())
        self.canvas.tag_bind(self.accoffcd1canvas, "<Button-1>" , lambda x: self.accessoffcd1())
        self.canvas.tag_bind(self.acconcd1canvas, "<Button-1>" , lambda x: self.accesscd1())

        self.boxcd2im = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.boxcd2 = self.canvas.create_image(
            210.0,
            124.0+p+p,
            image=self.boxcd2im
        )

        self.canvas.create_text(
            56.0,
            95.0+p+p,
            anchor="nw",
            text="CD2",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        self.camcd2im = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.cammacu = self.canvas.create_image(
            31.71429443359375,
            110.0+p+p,
            image=self.camcd2im
        )

        self.ctrloffcd2im = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.ctrloffcd2canvas = self.canvas.create_image(
            343.0,
            111.0+p+p,
            image=self.ctrloffcd2im
        )

        self.ctrloncd2im = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.ctrloncd2canvas = self.canvas.create_image(
            343.0,
            111.0+p+p,
            image=self.ctrloncd2im
        )

        self.accoffcd2im = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.accoffcd2canvas = self.canvas.create_image(
            211.0,
            112.0+p+p,
            image=self.accoffcd2im
        )

        self.acconcd2im = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.acconcd2canvas = self.canvas.create_image(
            211.0,
            112.0+p+p,
            image=self.acconcd2im
        )

        self.canvas.tag_bind(self.ctrloffcd2canvas, "<Button-1>" , lambda x: self.ctrloffcd2())
        self.canvas.tag_bind(self.ctrloncd2canvas, "<Button-1>" , lambda x: self.ctrloncd2btn())
        self.canvas.tag_bind(self.accoffcd2canvas, "<Button-1>" , lambda x: self.accessoffcd2())
        self.canvas.tag_bind(self.acconcd2canvas, "<Button-1>" , lambda x: self.accesscd2())
    
    def accessmcu(self):
        send(MCU_host,"MCU.camera_server()")
        threading.Thread(target=self.accessmcut).start()
        self.canvas.tag_raise(self.accoffmcucanvas)

    def accessmcut(self):
        camera_client = CameraClient(MCU_host)
        self.camera_clients.append(camera_client)
        time.sleep(2)
        camera_client.run()
        

    def accesscd1(self):
        send(CD1_host,"CD1.camera_server()")
        threading.Thread(target=self.accesscd1t).start()
        self.canvas.tag_raise(self.accoffcd1canvas)

    def accesscd1t(self):
        camera_client = CameraClient(CD1_host)
        self.camera_clients.append(camera_client)
        time.sleep(2)
        camera_client.run()

    def accesscd2(self):
        send(CD2_host,"CD2.camera_server()")
        threading.Thread(target=self.accesscd2t).start()
        self.canvas.tag_raise(self.accoffcd2canvas)

    def accesscd2t(self):
        camera_client = CameraClient(MCU_host)
        self.camera_clients.append(camera_client)
        time.sleep(2)
        camera_client.run()

    def accessoffmcu(self):
        if self.camera_clients:
            camera_client = self.camera_clients.pop(0)
            camera_client.on_close()
        self.canvas.tag_raise(self.acconmcucanvas)
        send(MCU_host,"MCU.camera_stop()")

    def accessoffcd1(self):
        if self.camera_clients:
            camera_client = self.camera_clients.pop(0)
            camera_client.on_close()
        self.canvas.tag_raise(self.acconcd1canvas)
        send(CD1_host,"CD1.camera_stop()")

    def accessoffcd2(self):
        if self.camera_clients:
            camera_client = self.camera_clients.pop(0)
            camera_client.on_close()
        self.canvas.tag_raise(self.acconcd2canvas)
        send(CD2_host,"CD2.camera_stop()")

    def ctrlonmcubtn(self):
        self.ctrlONdrone('MCU')
        self.ctrlonmcu = True
        self.canvas.tag_raise(self.ctrloffmcucanvas)
    
    def ctrloffmcu(self):
        self.ctrlonmcu = False
        self.canvas.tag_raise(self.ctrlonmcucanvas)

    def ctrloncd1btn(self):
        self.ctrlONdrone('CD1')
        self.ctrloncd1 = True
        self.canvas.tag_raise(self.ctrloffcd1canvas)
    
    def ctrloffcd1(self):
        self.ctrloncd1 = False
        self.canvas.tag_raise(self.ctrloncd1canvas)

    def ctrloncd2btn(self):
        self.ctrlONdrone('CD2')
        self.ctrloncd2 = True
        self.canvas.tag_raise(self.ctrloffcd2canvas)

    def ctrloffcd2(self):
        self.ctrloncd2 = False
        self.canvas.tag_raise(self.ctrloncd2canvas)


    def send_ctrl_drone(self,cmd):
        Velocity = 0.5
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

        if self.ctrlonmcu:
            send(MCU_host,f'MCU.send_ned_velocity({x},{y},{z})')
        if self.ctrloncd1:
            send(CD1_host,f'CD1.send_ned_velocity({x},{y},{z})')
        if self.ctrloncd2:
            send(CD2_host,f'CD2.send_ned_velocity({x},{y},{z})')

            
    def ctrlONdrone(self,drone):
        self.parent.bind('w', lambda event: command("ctrl_front(0.6)"))
        self.parent.bind('a', lambda event: command("ctrl_yaw(-1)"))
        self.parent.bind('d', lambda event: command("ctrl_yaw(1)"))
        self.parent.bind('l', lambda event: command('land()'))
        self.parent.bind('u', lambda event: self.send_ctrl_drone('u'))
        self.parent.bind('j', lambda event: self.send_ctrl_drone('j'))
        self.parent.bind('s', lambda event: self.send_ctrl_drone('s'))
        logger.log("CONTROL ON {}".format(drone))

    def ctrlOFFdrone(self,):
        self.parent.unbind('w')
        self.parent.unbind('a')
        self.parent.unbind('d')
        self.parent.unbind('u')
        self.parent.unbind('j')
        self.parent.unbind('s')
        logger.log("CONTROL OFF")

import tkinter as tk
from PIL import Image, ImageTk
import zmq
import threading
import io

class CameraClient:
    def __init__(self, host):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.connect(f"tcp://{host}:5522")

        self.running = False
        self.receive_thread = None
        self.latest_image = None

    def start_receiving(self):
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_images)
        self.receive_thread.start()

    def receive_images(self):
        try:
            while self.running:
                image_data = self.socket.recv()
                conf=self.socket.send_string('OK')

                image_array = cv2.imdecode(
                    np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR
                )

                # Update the latest image
                self.latest_image = image_array
                
        except Exception as e:
            print(f"Error receiving image: {e}")

    def update_image(self):
        # Check if there's a new image available
        if self.latest_image is not None:
            # Set the window to always stay on top
            cv2.namedWindow("Camera Client", cv2.WINDOW_NORMAL)
            
            cv2.imshow("Camera Client", self.latest_image)
            cv2.waitKey(1)
            
    def stop_receiving(self):
        self.running = False
        if self.receive_thread:
            self.receive_thread.join()

    def on_close(self):
        self.stop_receiving()

    def run(self):
        self.start_receiving()
        while self.running:
            # Update the image in the main loop
            self.update_image()