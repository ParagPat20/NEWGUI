from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame, Menu
from functions import *
from Initialize import INIT
from Missions import MISSION
from Edit_Mission import EDIT
from Devices import DEVICE
from Control import CTRL


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./MainWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainWindow():
    MAINW()

class MAINW(Toplevel):

    def bind_button_action(self, item, action):
        self.canvas.tag_bind(item, '<Button-1>', lambda event: action())
        
    def set_selected_mode(self, mode):
        self.selected_mode = mode
        logger.log("Selected Mode:{}".format(self.selected_mode))

    def show_mode_menu(self, event):
        self.menu.post(1473, 280)


    def mcuoffbtn(self):
        self.MCU_OFF_im = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.MCU_OFF = self.canvas.create_image(
            361.0,
            735.0,
            image=self.MCU_OFF_im
        )
        logger.log('MCUOFF')
        self.bind_button_action(self.MCU_OFF, self.mcuonbtn)
    def mcuonbtn(self):
        self.MCU_ON_im = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.MCU_ON = self.canvas.create_image(
            361.0,
            735.0,
            image=self.MCU_ON_im
        )
        logger.log('MCUON')
        self.bind_button_action(self.MCU_ON, self.mcuoffbtn)
    def cd1offbtn(self):
        self.CD1_OFF_im = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.CD1_OFF = self.canvas.create_image(
            446.0,
            735.0,
            image=self.CD1_OFF_im
        )
        self.bind_button_action(self.CD1_OFF, self.cd1onbtn)
    def cd1onbtn(self):
        self.CD1_ON_im = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.CD1_ON = self.canvas.create_image(
            446.0,
            735.0,
            image=self.CD1_ON_im
        )
        self.bind_button_action(self.CD1_ON, self.cd1offbtn)
    def cd2offbtn(self):
        self.CD2_OFF_im = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.CD2_OFF = self.canvas.create_image(
            531.0,
            735.0,
            image=self.CD2_OFF_im
        )
        self.bind_button_action(self.CD2_OFF, self.cd2onbtn)
    def cd2onbtn(self):
        self.CD2_ON_im = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.CD2_ON = self.canvas.create_image(
            531.0,
            735.0,
            image=self.CD2_ON_im
        )
        self.bind_button_action(self.CD2_ON, self.cd2offbtn)
    def cd3offbtn(self):
        self.CD3_OFF_im = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.CD3_OFF = self.canvas.create_image(
            616.0,
            735.0,
            image=self.CD3_OFF_im
        )
        self.bind_button_action(self.CD3_OFF, self.cd3onbtn)
    def cd3onbtn(self):
        self.CD3_ON_im = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.CD3_ON = self.canvas.create_image(
            616.0,
            735.0,
            image=self.CD3_ON_im
        )
        self.bind_button_action(self.CD3_ON, self.cd3offbtn)
    def cd4offbtn(self):
        self.CD4_OFF_im = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.CD4_OFF = self.canvas.create_image(
            701.0,
            735.0,
            image=self.CD4_OFF_im
        )
    def cd4onbtn(self):
        self.CD4_ON_im = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.CD4_ON = self.canvas.create_image(
            701.0,
            735.0,
            image=self.CD4_ON_im
        )
    def cd5offbtn(self):
        self.CD5_OFF_im = PhotoImage(
            file=relative_to_assets("image_15.png"))
        self.CD5_OFF = self.canvas.create_image(
            786.0,
            735.0,
            image=self.CD5_OFF_im
        )
    def cd5onbtn(self):
        self.CD5_ON_im = PhotoImage(
            file=relative_to_assets("image_16.png"))
        self.CD5_ON = self.canvas.create_image(
            786.0,
            735.0,
            image=self.CD5_ON_im
        )
    def multoffbtn(self):
        self.MULT_OFF_im = PhotoImage(
            file=relative_to_assets("image_17.png"))
        self.MULT_OFF = self.canvas.create_image(
            896.0,
            735.0,
            image=self.MULT_OFF_im
        )
    def multonbtn(self):
        self.MULT_ON_im = PhotoImage(
            file=relative_to_assets("image_18.png"))
        self.MULT_ON = self.canvas.create_image(
            896.0,
            735.0,
            image=self.MULT_ON_im
        )
    def armoffbtn(self):
        self.armoffim = PhotoImage(
            file=relative_to_assets("image_19.png"))
        self.armoff = self.canvas.create_image(
            1479.0,
            231.0,
            image=self.armoffim
        )
        self.bind_button_action(self.armoff, self.armonbtn)
    def armonbtn(self):
        self.armonim = PhotoImage(
            file=relative_to_assets("image_20.png"))
        self.armon = self.canvas.create_image(
            1479.0,
            231.0,
            image=self.armonim
        )
        self.bind_button_action(self.armon, self.armoffbtn)
            
    def modeoffbtn(self):
        self.modeoffim = PhotoImage(
            file=relative_to_assets("image_21.png"))
        self.modeoff = self.canvas.create_image(
            1473.0,
            284.0,
            image=self.modeoffim
        )
        self.bind_button_action(self.modeoff, self.modeonbtn)
        self.canvas.tag_bind(self.modeoff, '<Button-3>', self.show_mode_menu)
    def modeonbtn(self):
        self.modeonim = PhotoImage(
            file=relative_to_assets("image_22.png"))
        self.modeon = self.canvas.create_image(
            1473.0,
            284.0,
            image=self.modeonim
        )
        self.bind_button_action(self.modeon, self.modeoffbtn)
    def camoffbtn(self):
        self.camoffim = PhotoImage(
            file=relative_to_assets("image_23.png"))
        self.camoff = self.canvas.create_image(
            1467.0,
            337.0,
            image=self.camoffim
        )
        self.bind_button_action(self.camoff, self.camonbtn)
    def camonbtn(self):
        self.camonim = PhotoImage(
            file=relative_to_assets("image_24.png"))
        self.camon = self.canvas.create_image(
            1467.0,
            337.0,
            image=self.camonim
        )
        self.bind_button_action(self.camon, self.camoffbtn)
    def clawoffbtn(self):
        self.clawoffim = PhotoImage(
            file=relative_to_assets("image_25.png"))
        self.clawoff = self.canvas.create_image(
            1467.0,
            390.0,
            image=self.clawoffim
        )
        self.bind_button_action(self.clawoff, self.clawonbtn)
    def clawonbtn(self):
        self.clawonim = PhotoImage(
            file=relative_to_assets("image_26.png"))
        self.clawon = self.canvas.create_image(
            1467.0,
            390.0,
            image=self.clawonim
        )
        self.bind_button_action(self.clawon, self.clawoffbtn)
    def ctrloffbtn(self):
        self.ctrloffim = PhotoImage(
            file=relative_to_assets("image_27.png"))
        self.ctrloff = self.canvas.create_image(
            1463.0,
            443.0,
            image=self.ctrloffim
        )
        self.bind_button_action(self.ctrloff, self.ctrlonbtn)
    def ctrlonbtn(self):
        self.ctrlonim = PhotoImage(
            file=relative_to_assets("image_28.png"))
        self.ctrlon = self.canvas.create_image(
            1463.0,
            443.0,
            image=self.ctrlonim
        )
        self.bind_button_action(self.ctrlon, self.ctrloffbtn)
    def tkoffoffbtn(self):
        self.tkoffoffim = PhotoImage(
            file=relative_to_assets("image_29.png"))
        self.tkoffoff = self.canvas.create_image(
            1462.0,
            496.0,
            image=self.tkoffoffim
        )
        self.bind_button_action(self.tkoffoff, self.tkoffonbtn)
    def tkoffonbtn(self):
        self.tkoffonim = PhotoImage(
            file=relative_to_assets("image_30.png"))
        self.tkoffon = self.canvas.create_image(
            1462.0,
            496.0,
            image=self.tkoffonim
        )
        self.bind_button_action(self.tkoffon, self.tkoffoffbtn)
    def posoffbtn(self):
        self.posoffim = PhotoImage(
            file=relative_to_assets("image_31.png"))
        self.posoff = self.canvas.create_image(
            1462.0,
            549.0,
            image=self.posoffim
        )
        self.bind_button_action(self.posoff, self.posonbtn)
    def posonbtn(self):
        self.posonim = PhotoImage(
            file=relative_to_assets("image_32.png"))
        self.poson = self.canvas.create_image(
            1462.0,
            549.0,
            image=self.posonim
        )
        self.bind_button_action(self.poson, self.posoffbtn)
    def landoffbtn(self):
        self.landoffim = PhotoImage(
            file=relative_to_assets("image_33.png"))
        self.landoff = self.canvas.create_image(
            1471.0,
            602.0,
            image=self.landoffim
        )
        self.bind_button_action(self.landoff, self.landonbtn)
    def landonbtn(self):
        self.landonim = PhotoImage(
            file=relative_to_assets("image_34.png"))
        self.landon = self.canvas.create_image(
            1471.0,
            602.0,
            image=self.landonim
        )
        self.bind_button_action(self.landon, self.landoffbtn)
    def mcuentry(self):
        self.entry_mcu_im_im = PhotoImage(
            file=relative_to_assets("image_35.png"))
        self.entry_mcu_im = self.canvas.create_image(
            1184.0,
            596.0,
            image=self.entry_mcu_im_im
        )
        self.entry_mcu_bg = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            1184.0,
            596.0,
            image=self.entry_mcu_bg
        )
        self.entry_mcu = Entry(
            bd=0,
            bg="#353535",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_mcu.place(
            x=1016.0,
            y=580.0,
            width=336.0,
            height=30.0
        )
    def cd1entry(self):
        self.entry_cd1_im_im = PhotoImage(
            file=relative_to_assets("image_36.png"))
        self.entry_mcu_im = self.canvas.create_image(
            1184.0,
            527.0,
            image=self.entry_mcu_im_im
        )

        self.entry_cd1_bg = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            1184.0,
            527.0,
            image=self.entry_cd1_bg
        )
        self.entry_cd1 = Entry(
            bd=0,
            bg="#353535",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_cd1.place(
            x=1016.0,
            y=511.0,
            width=336.0,
            height=30.0
        )
    def cd2entry(self):
        self.entry_cd2_im_im = PhotoImage(
            file=relative_to_assets("image_37.png"))
        self.entry_cd2_im = self.canvas.create_image(
            1184.0,
            458.0,
            image=self.entry_cd2_im_im
        )

        self.entry_bg3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            1184.0,
            458.0,
            image=self.entry_bg3
        )
        self.entry_cd2 = Entry(
            bd=0,
            bg="#353535",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_cd2.place(
            x=1016.0,
            y=442.0,
            width=336.0,
            height=30.0
        )
 
        

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("RoboControllo")
        
        self.current_window = None
        self.ctrl_window = CTRL(self)
        self.miss_window = MISSION(self)
        self.init_window = INIT(self)
        self.edit_window = EDIT(self)

        self.geometry("1500x760+5+0")
        self.configure(bg = "#000000")
        self.connected_drones = []
        self.MCU_OFF = None
        self.MCU_ON = None
        self.CD1_OFF = None
        self.CD1_ON = None
        self.CD2_OFF = None
        self.CD2_ON = None
        self.CD3_OFF = None
        self.CD3_ON = None
        
        self.canvas = Canvas(
            self,
            bg = "#000000",
            height = 760,
            width = 1500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.menu = Menu(self.canvas, tearoff=0, font=("Montserrat Bold", 16))

        modes = ["GUIDED", "STABILIZE", "RTL", "BREAK", "LAND", "AUTOTUNE"]
        for mode in modes:
            self.menu.add_command(
                label=mode, command=lambda m=mode: self.set_selected_mode(m))

        

        self.indicator = Frame(self, background="#FFFFFF")
        self.indicator.place(x=0, y=60, height = 30, width = 4)

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            750.0,
            17.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            24.0,
            397.0,
            image=self.image_image_3
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.ctrl_btn = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.ctrl_btn, "ctrl"),
            relief="flat", activebackground="#353535"
        )
        self.ctrl_btn.place(
            x=9.0,
            y=195.0,
            width=30.0,
            height=30.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.set_btn = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.set_btn, "init"),
            relief="flat", activebackground="#353535"
        )
        self.set_btn.place(
            x=9.0,
            y=152.0,
            width=30.0,
            height=30.0
        )


        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.mis_btn = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.mis_btn, "mis"),
            relief="flat", activebackground="#353535"
        )
        self.mis_btn.place(
            x=9.0,
            y=106.0,
            width=30.0,
            height=30.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.init_btn = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.init_btn, "init"),
            relief="flat", activebackground="#353535"
        )
        self.init_btn.place(
            x=9.0,
            y=60.0,
            width=30.0,
            height=30.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.menu_btn = Button(self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.menu_btn, "menu"),
            relief="flat", activebackground="#353535"
        )
        self.menu_btn.place(
            x=9.0,
            y=2.0,
            width=30.0,
            height=30.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            1245.0,
            700.0,
            image=self.image_image_4
        )

        self.log_text = Text(
            self.canvas,
            wrap="word",
            font=("Montserrat Bold", 5),
            bg="#4A4848",
            relief="flat",
            state="disabled"
        )

        self.map_app = MapApplication(self)
        self.map_app.map_widget.place(x=-13.0, y=-70.0, width=1360.0, height=550.0)

        self.armoffbtn()
        self.modeoffbtn()
        self.camoffbtn()
        self.clawoffbtn()
        self.ctrloffbtn()
        self.tkoffoffbtn()
        self.posoffbtn()
        self.landoffbtn()



        self.log_text.place(x=990, y=660, width=510, height=80)

        logger.set_log_text(self.log_text)
        logging_thread = threading.Thread(target=start_logging_in_background)
        logging_thread.start()

        self.current_window_device = DEVICE(self)

        self.windows = {

            "init" : INIT(self),
            "devi" : DEVICE(self),
            "mis" : MISSION(self),
            "edit" : EDIT(self),
            "ctrl" : CTRL(self)

        }

        if 'MCU' in self.connected_drones:
            
            self.mcuentry()

        if 'CD1' in self.connected_drones:
 
            self.cd1entry()
        
        if 'CD2' in self.connected_drones:

            self.cd2entry()


        self.resizable(True, True)
        self.mainloop()

    def place_indicator(self):
        pass

    def handle_btn_press(self, caller, name):
        try:
            self.indicator.place(x=0, y=caller.winfo_y())

            # Destroy existing windows before creating new ones
            if name == 'init':
                if self.init_window:
                    self.init_window.destroy()
                self.init_window = INIT(self)
                self.init_window.place(x=49, y=35, width=420.0, height=725.0)
            elif name == 'mis':
                if self.miss_window:
                    self.miss_window.destroy()
                self.miss_window = MISSION(self)
                self.miss_window.place(x=49, y=35, width=420.0, height=725.0)
            elif name == 'ctrl':
                if self.ctrl_window:
                    self.ctrl_window.destroy()
                self.ctrl_window = CTRL(self)
                self.ctrl_window.place(x=49, y=35, width=420.0, height=725.0)
            elif name == 'devi':
                if self.init_window.overlay_win:
                    self.init_window.overlay_win.destroy()
                self.init_window.overlay_win = DEVICE(self)
                self.init_window.overlay_win.place(x=645, y=135, width=600.0, height=456.0)
            elif name == 'edit':
                if self.edit_window:
                    self.edit_window.destroy()
                self.edit_window = EDIT(self)
                self.edit_window.place(x=49, y=35, width=420.0, height=725.0)
            elif name =='menu':
                if self.init_window:
                    self.init_window.destroy()
                if self.miss_window:
                    self.miss_window.destroy()
                if self.ctrl_window:
                    self.ctrl_window.destroy()
                if self.edit_window:
                    self.edit_window.destroy()

        except Exception as e:
            logger.log("Handle_error= {}".format(e))

    