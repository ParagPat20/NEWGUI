##### MCU

from pathlib import Path
from tkinter import Button, PhotoImage
from functions import *


x = 120
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Initialize")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MCU:
    def __init__(self,canvas):
        self=canvas

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            210.0,
            219.0,
            image=self.image_image_1
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

class CD1:
    def __init__(self,canvas):
        self=canvas
        self.image_image_1_2 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1_2 = self.canvas.create_image(
            210.0,
            219.0+x,
            image=self.image_image_1_2
        )

        # Battery Image

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

        # Mode Image

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

        # Speed Image

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

        # Drone Image

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

class CD2:
    def __init__(self,canvas):
        self=canvas
        self.image_image_1_3 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1_3 = self.canvas.create_image(
            210.0,
            219.0+x+x,
            image=self.image_image_1_3
        )


        # Battery Image

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

        # Mode Image

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

        # Speed Image

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

        # Drone Image

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
        # Disconnect to Drone Button

        self.button_image_22 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_22 = Button(self.canvas,
            image=self.button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
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

class CD4():
    def __init__(self,canvas):


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
            text="CD3",
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




