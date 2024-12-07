from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from functions import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Devices")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def devices():
    DEVICE()

class DEVICE(Frame):

    def save_device(self):
        global json_data
        
        drone_name = self.entry_3.get()
        send(hosts[drone_name],f"initialize_{drone_name}")
        logger.log("Initializing {} Drone".format(drone_name))
        json_data["connected_devices"] +=1

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


        self.configure(bg = "#1C1C1D")


        self.canvas = Canvas(
            self,
            bg = "#1C1C1D",
            height = 456,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            300.0,
            311.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            300.0,
            319.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self,
            bd=0,
            bg="#333333",
            fg="#CDCDCD",
            highlightthickness=0
        )
        self.entry_1.place(
            x=89.0,
            y=308.0,
            width=422.0,
            height=21.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            300.0,
            216.0,
            image=self.image_image_2
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            300.0,
            224.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(self,
            bd=0,
            bg="#333333",
            fg="#CDCDCD",
            highlightthickness=0
        )
        self.entry_2.place(
            x=89.0,
            y=213.0,
            width=422.0,
            height=21.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            300.0,
            121.0,
            image=self.image_image_3
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            300.0,
            129.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(self,
            bd=0,
            bg="#333333",
            fg="#CDCDCD",
            highlightthickness=0
        )
        self.entry_3.place(
            x=89.0,
            y=118.0,
            width=422.0,
            height=21.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.save_device(),
            activebackground="#1C1C1D",
            relief="raised"
        )
        self.button_1.place(
            x=435.0,
            y=379.0,
            width=104.0,
            height=54.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.init_window.overlay_win.destroy(),
            activebackground="#1C1C1D",
            relief="raised"
        )
        self.button_2.place(
            x=270.0,
            y=376.0,
            width=170.0,
            height=62.0
        )

        self.canvas.create_rectangle(
            -1.999908447265625,
            46.75,
            600.0007019042969,
            48.75,
            fill="#636363",
            outline="")

        self.canvas.create_text(
            9.0,
            6.0,
            anchor="nw",
            text="Add Device",
            fill="#CDCDCD",
            font=("Inter Black", 16 * -1)
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.init_window.overlay_win.destroy(),
            activebackground="#1C1C1D",
            relief="raised"
        )
        self.button_3.place(
            x=551.0,
            y=9.0,
            width=37.0,
            height=35.0
        )
