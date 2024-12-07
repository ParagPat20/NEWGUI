from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar
from functions import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Missions")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def missions():
    MISSION()

class MISSION(Frame):

    def __init__(self, parent, *args, **kwargs):
        global mission
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mission_name = mission[0]

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

        self.canvas.place(x = 0, y = 0)
        self.overlay_win_active = False
        
        self.canvas.create_rectangle(
            0.0,
            0.0,
            420.0,
            725.0,
            fill="#2A282C",
            outline="")

        self.canvas.create_text(
            174.0,
            16.0,
            anchor="nw",
            text="Missions",
            fill="#FFFFFF",
            font=("CaveatRoman Regular", 24 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            210.0,
            156.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            76.0,
            135.0,
            image=self.image_image_2
        )

        self.mission_name_label = self.canvas.create_text(
            96.0,
            122.0,
            anchor="nw",
            text=self.mission_name,
            fill="#CDCDCD",
            font=("IBMPlexMono Bold", 20 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            143.0,
            178.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            159.0,
            172.0,
            anchor="nw",
            text="100m",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 11 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            249.0,
            179.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            264.0,
            172.0,
            anchor="nw",
            text="10m",
            fill="#CDCDCD",
            font=("IBMPlexMono Medium", 11 * -1)
        )

        self.button_1 = Button(
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat", activebackground="#2A282C"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=0,
            height=0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            43.0,
            156.0,
            image=self.image_image_5
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat", activebackground="#2A282C"
        )
        self.button_2.place(
            x=194.0,
            y=121.0,
            width=29.0,
            height=28.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat", activebackground="#2A282C"
        )
        self.button_3.place(
            x=386.0,
            y=8.0,
            width=26.0,
            height=26.0
        )


        self.button_4 = Button(
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.handle_btn_press(self.parent.mis_btn, "edit"),
            relief="flat", activebackground="#2A282C"
        )


        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            377.0,
            156.0,
            image=self.image_image_6
        )

        self.canvas.tag_bind(self.image_5, "<Button-1>", lambda event: self.button_1.invoke())
        self.canvas.tag_bind(self.image_6, "<Button-1>", lambda event: self.button_4.invoke())
