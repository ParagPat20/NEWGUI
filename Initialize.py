from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Scrollbar
from functions import *
from Devices import DEVICE

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Initialize")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def initialize():
    INIT()

x = 120

class INIT(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg = "#2A282C")
        
# Made Canvas
        self.canvas = Canvas(
            self,
            bg = "#2A282C",
            height = 725,
            width = 420,
            bd = 0,
            highlightthickness = 0,
            relief = "flat"
        )

        self.canvas.place(x = 0, y = 0)
# Rectangle around whole Page
        self.canvas.create_rectangle(
            0.0,
            0.0,
            420.0,
            725.0,
            fill="#2A282C",
            outline="")
        
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Place the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Create a frame within the canvas to hold scrollable content
        self.scrollable_frame = Frame(self.canvas, bg="#2A282C")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
# Button - Add Devices
        self.overlay_win_active = False
        self.overlay_win = DEVICE(self)
        

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.device_btn_press(),
            relief="flat", activebackground="#2A282C"
        )
        self.button_1.place(
            x=102.0,
            y=61.0,
            width=215.0,
            height=32.9959716796875
        )

        self.drone_numbers=self.canvas.create_text(
            133.0,
            106.0,
            anchor="nw",
            text=f"Drone(s) Connected: {json_data['connected_devices']}/6",
            fill="#FFFFFF",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            180.0,
            19.0,
            anchor="nw",
            text="Drones",
            fill="#FFFFFF",
            font=("CaveatRoman Regular", 24 * -1)
        )
        

# Image of boundary that contains drone information

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            210.0,
            219.0,
            image=self.image_image_1
        )
        

        self.image_image_1_2 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1_2 = self.canvas.create_image(
            210.0,
            219.0+x,
            image=self.image_image_1_2
        )

        self.image_image_1_3 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1_3 = self.canvas.create_image(
            210.0,
            219.0+x+x,
            image=self.image_image_1_3
        )

        self.image_image_1_4 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1_4 = self.canvas.create_image(
            210.0,
            219.0+x+x+x,
            image=self.image_image_1_4
        )

# Battery Image

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            37.0,
            253.0,
            image=self.image_image_2
        )

        self.mcu_bat=self.canvas.create_text(
            47.0,
            244.0,
            anchor="nw",
            text="100%",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 13 * -1)
        )

        self.image_image_2_1 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2_1 = self.canvas.create_image(
            37.0,
            253.0+x,
            image=self.image_image_2_1
        )

        self.cd1_bat=self.canvas.create_text(
            47.0,
            244.0+x,
            anchor="nw",
            text="100%",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 13 * -1)
        )

        self.image_image_2_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2_2 = self.canvas.create_image(
            37.0,
            253.0+x+x,
            image=self.image_image_2_2
        )

        self.cd2_bat=self.canvas.create_text(
            47.0,
            244.0+x+x,
            anchor="nw",
            text="100%",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 13 * -1)
        )

        self.image_image_2_3 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2_3 = self.canvas.create_image(
            37.0,
            253.0+x+x+x,
            image=self.image_image_2_3
        )

        cd3_bat=self.canvas.create_text(
            47.0,
            244.0+x+x+x,
            anchor="nw",
            text="100%",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 13 * -1)
        )

# Mode Image

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            166.0,
            253.0,
            image=self.image_image_3
        )

        self.mcu_mode=self.canvas.create_text(
            179.0,
            244.0,
            anchor="nw",
            text="Mode",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        self.image_image_3_1 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3_1 = self.canvas.create_image(
            166.0,
            253.0+x,
            image=self.image_image_3_1
        )

        self.cd1_mode=self.canvas.create_text(
            179.0,
            244.0+x,
            anchor="nw",
            text="Mode",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        self.image_image_3_2 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3_2 = self.canvas.create_image(
            166.0,
            253.0+x+x,
            image=self.image_image_3_2
        )

        self.cd2_mode=self.canvas.create_text(
            179.0,
            244.0+x+x,
            anchor="nw",
            text="Mode",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        self.image_image_3_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3_3 = self.canvas.create_image(
            166.0,
            253.0+x+x+x,
            image=self.image_image_3_3
        )

        self.cd3_mode=self.canvas.create_text(
            179.0,
            244.0+x+x+x,
            anchor="nw",
            text="Mode",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

# Speed Image

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            293.0,
            253.0,
            image=self.image_image_4
        )

        self.mcu_gs=self.canvas.create_text(
            304.0,
            244.0,
            anchor="nw",
            text="0.0 m/s",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        self.image_image_41 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_41 = self.canvas.create_image(
            293.0,
            253.0+x,
            image=self.image_image_41
        )

        self.cd1_gs=self.canvas.create_text(
            304.0,
            244.0+x,
            anchor="nw",
            text="0.0 m/s",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        self.image_image_42 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_42 = self.canvas.create_image(
            293.0,
            253.0+x+x,
            image=self.image_image_42
        )

        self.cd2_gs=self.canvas.create_text(
            304.0,
            244.0+x+x,
            anchor="nw",
            text="0.0 m/s",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        self.image_image_43 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_43 = self.canvas.create_image(
            293.0,
            253.0+x+x+x,
            image=self.image_image_43
        )

        self.cd3_gs=self.canvas.create_text(
            304.0,
            244.0+x+x+x,
            anchor="nw",
            text="0.0 m/s",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

# Drone Image

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            31.71429443359375,
            196.0,
            image=self.image_image_5
        )

        self.canvas.create_text(
            56.0,
            181.0,
            anchor="nw",
            text="MCU",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        self.image_image_51 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_51 = self.canvas.create_image(
            31.71429443359375,
            196.0+x,
            image=self.image_image_51
        )

        self.canvas.create_text(
            56.0,
            181.0+x,
            anchor="nw",
            text="CD1",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        self.image_image_52 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_52 = self.canvas.create_image(
            31.71429443359375,
            196.0+x+x,
            image=self.image_image_52
        )

        self.canvas.create_text(
            56.0,
            181.0+x+x,
            anchor="nw",
            text="CD2",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        self.image_image_53 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_53 = self.canvas.create_image(
            31.71429443359375,
            196.0+x+x+x,
            image=self.image_image_53
        )

        self.canvas.create_text(
            56.0,
            181.0+x+x+x,
            anchor="nw",
            text="CD3",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

# Disconnect to Drone Button

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.disconnect("MCU"),
            relief="flat", activebackground="#353535"
        )
        self.button_2.place(
            x=244.0,
            y=175.0,
            width=155.0,
            height=44.0
        )

# Connect to Drone Button
        
        if json_data['mcuconnected'] == False:

            self.button_image_3 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_3 = Button(self.canvas,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("MCU"),
                relief="flat", activebackground="#353535"
            )
            self.button_3.place(
                x=246.0,
                y=175.0,
                width=155.0,
                height=44.0
            )

# Disconnect to Drone Button

        self.button_image_21 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_21 = Button(self.canvas,
            image=self.button_image_21,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.disconnect("CD1"), 
            relief="flat", activebackground="#353535"
        )
        self.button_21.place(
            x=244.0,
            y=175.0+x,
            width=155.0,
            height=44.0
        )

# Connect to Drone Button
        
        if json_data['cd1connected'] == False:

            self.button_image_31 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_31 = Button(self.canvas,
                image=self.button_image_31,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD1"),
                relief="flat", activebackground="#353535"
            )
            self.button_31.place(
                x=246.0,
                y=175.0+x,
                width=155.0,
                height=44.0
            )

# Disconnect to Drone Button

        self.button_image_22 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_22 = Button(self.canvas,
            image=self.button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.disconnect("CD2"),
            relief="flat", activebackground="#353535"
        )
        self.button_22.place(
            x=244.0,
            y=175.0+x+x,
            width=155.0,
            height=44.0
        )

# Connect to Drone Button
        
        if json_data['cd2connected'] == False:

            self.button_image_32 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_32 = Button(self.canvas,
                image=self.button_image_32,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD2"),
                relief="flat", activebackground="#353535"
            )
            self.button_32.place(
                x=246.0,
                y=175.0+x+x,
                width=155.0,
                height=44.0
            )

# Disconnect to Drone Button

        self.button_image_23 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_23 = Button(self.canvas,
            image=self.button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.disconnect("CD3"),
            relief="flat", activebackground="#353535"
        )
        self.button_23.place(
            x=244.0,
            y=175.0+x+x+x,
            width=155.0,
            height=44.0
        )

# Connect to Drone Button
        
        if json_data['cd3connected'] == False:

            self.button_image_33 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_33 = Button(self.canvas,
                image=self.button_image_33,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD3"),
                relief="flat", activebackground="#353535"
            )
            self.button_33.place(
                x=246.0,
                y=175.0+x+x+x,
                width=155.0,
                height=44.0
            )


        self.image_image_1_5 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1_5 = self.canvas.create_image(
            210.0,
            219.0+x+x+x+x,
            image=self.image_image_1_5
        )


        # Battery Image

        self.image_image_2_4 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2_4 = self.canvas.create_image(
            37.0,
            253.0+x+x+x+x,
            image=self.image_image_2_4
        )

        cd4_bat=self.canvas.create_text(
            47.0,
            244.0+x+x+x+x,
            anchor="nw",
            text="100%",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 13 * -1)
        )

        # Mode Image

        self.image_image_3_4 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3_4 = self.canvas.create_image(
            166.0,
            253.0+x+x+x+x,
            image=self.image_image_3_4
        )

        self.cd3_mode=self.canvas.create_text(
            179.0,
            244.0+x+x+x+x,
            anchor="nw",
            text="Mode",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        # Speed Image

        self.image_image_44 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_44 = self.canvas.create_image(
            293.0,
            253.0+x+x+x+x,
            image=self.image_image_44
        )

        self.cd4_gs=self.canvas.create_text(
            304.0,
            244.0+x+x+x+x,
            anchor="nw",
            text="0.0 m/s",
            fill="#CDCDCD",
            font=("IBMPlexMono Regular", 13 * -1)
        )

        # Drone Image

        self.image_image_54 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_53 = self.canvas.create_image(
            31.71429443359375,
            196.0+x+x+x+x,
            image=self.image_image_54
        )

        self.canvas.create_text(
            56.0,
            181.0+x+x+x+x,
            anchor="nw",
            text="CD4",
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 24 * -1)
        )

        # Disconnect to Drone Button

        self.button_image_24 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_24 = Button(self.canvas,
            image=self.button_image_24,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.disconnect("CD4"),
            relief="flat", activebackground="#353535"
        )
        self.button_24.place(
            x=244.0,
            y=175.0+x+x+x+x,
            width=155.0,
            height=44.0
        )

# Connect to Drone Button
        
        if json_data['cd4connected'] == False:

            self.button_image_34 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_34 = Button(self.canvas,
                image=self.button_image_34,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD4"),
                relief="flat", activebackground="#353535"
            )
            self.button_34.place(
                x=246.0,
                y=175.0+x+x+x+x,
                width=155.0,
                height=44.0
            )


# Restart Button

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: json_data_reset,
            relief="flat", activebackground="#2A282C"
        )
        self.button_4.place(
            x=380.0,
            y=12.0,
            width=30.0,
            height=30.0
        )



    def connect(self,drone):
        
        if drone == 'MCU':
            send(MCU_host, 'initialize_MCU()')
            self.button_3.destroy()
            self.parent.mcuoffbtn()
            json_data["mcuconnected"] = True
            json_data["connected_devices"] += 1
            self.parent.mcuentry()
            self.button_image_2 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            self.button_2 = Button(self.canvas,
                image=self.button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.disconnect("MCU"),
                relief="flat", activebackground="#353535"
            )
            self.button_2.place(
                x=244.0,
                y=175.0,
                width=155.0,
                height=44.0
            )


        if drone == 'CD1':
            send(CD1_host, 'initialize_CD1()')
            self.button_31.destroy()
            self.parent.cd1offbtn()
            json_data["cd1connected"] = True
            json_data["connected_devices"] += 1
            self.parent.cd1entry()
            self.button_image_21 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            self.button_21 = Button(self.canvas,
                image=self.button_image_21,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.disconnect("CD1"),
                relief="flat", activebackground="#353535"
            )
            self.button_21.place(
                x=244.0,
                y=175.0+x,
                width=155.0,
                height=44.0
            )

            
        if drone == 'CD2':
            send(CD2_host, 'initialize_CD2()')
            self.button_32.destroy()
            self.parent.cd2offbtn()
            json_data["cd2connected"] = True
            json_data["connected_devices"] += 1
            self.parent.cd2entry()
            self.button_image_22 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            self.button_22 = Button(self.canvas,
                image=self.button_image_22,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.disconnect("CD2"),
                relief="flat", activebackground="#353535"
            )
            self.button_22.place(
                x=244.0,
                y=175.0+x+x,
                width=155.0,
                height=44.0
            )

        
        if drone == 'CD3':
            send(CD3_host, 'initialize_CD3()')
            self.button_33.destroy()
            self.parent.cd3offbtn()
            json_data["cd3connected"] = True
            json_data["connected_devices"] += 1
            self.button_image_23 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            self.button_23 = Button(self.canvas,
                image=self.button_image_23,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.disconnect("CD3"),
                relief="flat", activebackground="#353535"
            )
            self.button_23.place(
                x=244.0,
                y=175.0+x+x+x,
                width=155.0,
                height=44.0
            )
        if drone == 'CD4':
            send(CD4_host, 'initialize_CD4()')
            self.button_34.destroy()
            self.parent.cd4offbtn()
            json_data["cd4connected"] = True
            json_data["connected_devices"] += 1
            self.button_image_24 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            self.button_24 = Button(self.canvas,
                image=self.button_image_24,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.disconnect("CD4"),
                relief="flat", activebackground="#353535"
            )
            self.button_24.place(
                x=244.0,
                y=175.0+x+x+x+x,
                width=155.0,
                height=44.0
            )


        logger.log("initializing {}".format(drone))
        self.parent.connected_drones.append(drone)

    def disconnect(self,drone):
        
        if drone == 'MCU':
            send(MCU_host, 'deinitialize_MCU()')
            self.button_2.destroy()
            try:
                if self.parent.MCU_OFF:
                    self.parent.canvas.delete(self.parent.MCU_OFF)
                if self.parent.MCU_ON:
                    self.parent.canvas.delete(self.parent.MCU_ON)
            except Exception as e:
                pass
            json_data["mcuconnected"] = False
            json_data["connected_devices"] -= 1

            self.button_image_3 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_3 = Button(self.canvas,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("MCU"),
                relief="flat", activebackground="#353535"
            )
            self.button_3.place(
                x=246.0,
                y=175.0,
                width=155.0,
                height=44.0
            )


        if drone == 'CD1':
            send(CD1_host, 'deinitialize_CD1()')
            self.button_21.destroy()
            try:
                if self.parent.CD1_OFF:
                    self.parent.canvas.delete(self.parent.CD1_OFF)
                if self.parent.CD1_ON:
                    self.parent.canvas.delete(self.parent.CD1_ON)
            except Exception as e:
                pass
            json_data["cd1connected"] = False
            json_data["connected_devices"] -= 1
            
            self.button_image_31 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_31 = Button(self.canvas,
                image=self.button_image_31,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD1"),
                relief="flat", activebackground="#353535"
            )
            self.button_31.place(
                x=246.0,
                y=175.0+x,
                width=155.0,
                height=44.0
            )
            
        if drone == 'CD2':
            send(CD2_host, 'deinitialize_CD2()')
            self.button_22.destroy()
            try:
                if self.parent.CD2_OFF:
                    self.parent.canvas.delete(self.parent.CD2_OFF)
                if self.parent.CD2_ON:
                    self.parent.canvas.delete(self.parent.CD2_ON)
            except Exception as e:
                pass
            json_data["cd2connected"] = False
            json_data["connected_devices"] -= 1
            
            self.button_image_32 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_32 = Button(self.canvas,
                image=self.button_image_32,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD2"),
                relief="flat", activebackground="#353535"
            )
            self.button_32.place(
                x=246.0,
                y=175.0+x+x,
                width=155.0,
                height=44.0
            )
        
        if drone == 'CD3':
            send(CD3_host, 'deinitialize_CD3()')
            self.button_23.destroy()
            try:
                if self.parent.CD3_OFF:
                    self.parent.canvas.delete(self.parent.CD3_OFF)
                if self.parent.CD3_ON:
                    self.parent.canvas.delete(self.parent.CD3_ON)
            except Exception as e:
                pass
            json_data["cd3connected"] = False
            json_data["connected_devices"] -= 1
            
            self.button_image_33 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_33 = Button(self.canvas,
                image=self.button_image_33,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD3"),
                relief="flat", activebackground="#353535"
            )
            self.button_33.place(
                x=246.0,
                y=175.0+x+x+x,
                width=155.0,
                height=44.0
            )

        if drone == 'CD4':
            send(CD4_host, 'deinitialize_CD4()')
            self.button_24.destroy()
            try:
                if self.parent.CD4_OFF:
                    self.parent.canvas.delete(self.parent.CD4_OFF)
                if self.parent.CD4_ON:
                    self.parent.canvas.delete(self.parent.CD4_ON)
            except Exception as e:
                pass
            json_data["cd4connected"] = False
            json_data["connected_devices"] -= 1
            
            self.button_image_34 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            self.button_34 = Button(self.canvas,
                image=self.button_image_34,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.connect("CD4"),
                relief="flat", activebackground="#353535"
            )
            self.button_34.place(
                x=246.0,
                y=175.0+x+x+x+x,
                width=155.0,
                height=44.0
            )

        logger.log("deinitializing {}".format(drone))
        self.parent.connected_drones.remove(drone)
            
    def device_btn_press(self):
        if self.overlay_win:
            self.overlay_win.destroy()
        self.overlay_win = DEVICE(self)
        self.parent.handle_btn_press(self.parent.init_btn,"devi")
        