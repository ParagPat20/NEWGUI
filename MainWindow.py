from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame, Menu, font
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
        self.menu.post(1343, 280)

    def show_ctrl_menu(self, event):
        self.ctrl_menu.post(1343, 440)

    def ctrl_menu_action(self, mode):
        self.control_type = mode
        logger.log("Selected Ctrl Mode: {}".format(mode))


    def mcuoffbtn(self):
        self.MCU_OFF_im = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.MCU_OFF = self.canvas.create_image(
            361.0,
            735.0,
            image=self.MCU_OFF_im
        )
        self.bind_button_action(self.MCU_OFF, self.mcuonbtn)
        select_drone('MCU',False)

    def mcuonbtn(self):
        self.MCU_ON_im = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.MCU_ON = self.canvas.create_image(
            361.0,
            735.0,
            image=self.MCU_ON_im
        )
        self.bind_button_action(self.MCU_ON, self.mcuoffbtn)
        select_drone('MCU',True)

    def cd1offbtn(self):
        self.CD1_OFF_im = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.CD1_OFF = self.canvas.create_image(
            446.0,
            735.0,
            image=self.CD1_OFF_im
        )
        self.bind_button_action(self.CD1_OFF, self.cd1onbtn)
        select_drone('CD1',False)

    def cd1onbtn(self):
        self.CD1_ON_im = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.CD1_ON = self.canvas.create_image(
            446.0,
            735.0,
            image=self.CD1_ON_im
        )
        self.bind_button_action(self.CD1_ON, self.cd1offbtn)
        select_drone('CD1',True)

    def cd2offbtn(self):
        self.CD2_OFF_im = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.CD2_OFF = self.canvas.create_image(
            531.0,
            735.0,
            image=self.CD2_OFF_im
        )
        self.bind_button_action(self.CD2_OFF, self.cd2onbtn)
        select_drone('CD2',False)

    def cd2onbtn(self):
        self.CD2_ON_im = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.CD2_ON = self.canvas.create_image(
            531.0,
            735.0,
            image=self.CD2_ON_im
        )
        self.bind_button_action(self.CD2_ON, self.cd2offbtn)
        select_drone('CD2',True)
    def cd3offbtn(self):
        self.CD3_OFF_im = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.CD3_OFF = self.canvas.create_image(
            616.0,
            735.0,
            image=self.CD3_OFF_im
        )
        self.bind_button_action(self.CD3_OFF, self.cd3onbtn)
        select_drone('CD3',False)
    def cd3onbtn(self):
        self.CD3_ON_im = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.CD3_ON = self.canvas.create_image(
            616.0,
            735.0,
            image=self.CD3_ON_im
        )
        self.bind_button_action(self.CD3_ON, self.cd3offbtn)
        select_drone('CD3',True)
    def cd4offbtn(self):
        self.CD4_OFF_im = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.CD4_OFF = self.canvas.create_image(
            701.0,
            735.0,
            image=self.CD4_OFF_im
        )
        self.bind_button_action(self.CD4_OFF, self.cd4onbtn)
        select_drone('CD4',False)
    def cd4onbtn(self):
        self.CD4_ON_im = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.CD4_ON = self.canvas.create_image(
            701.0,
            735.0,
            image=self.CD4_ON_im
        )
        self.bind_button_action(self.CD4_ON, self.cd4offbtn)
        select_drone('CD4',True)
    def cd5offbtn(self):
        self.CD5_OFF_im = PhotoImage(
            file=relative_to_assets("image_15.png"))
        self.CD5_OFF = self.canvas.create_image(
            786.0,
            735.0,
            image=self.CD5_OFF_im
        )
        self.bind_button_action(self.CD5_OFF, self.cd5onbtn)
        select_drone('CD5',False)

    def cd5onbtn(self):
        self.CD5_ON_im = PhotoImage(
            file=relative_to_assets("image_16.png"))
        self.CD5_ON = self.canvas.create_image(
            786.0,
            735.0,
            image=self.CD5_ON_im
        )
        self.bind_button_action(self.CD5_ON, self.cd5offbtn)
        select_drone('CD5',True)










    def armoffbtn(self):
        self.armoffim = PhotoImage(
            file=relative_to_assets("image_19.png"))
        self.armoff = self.canvas.create_image(
            1479.0,
            231.0,
            image=self.armoffim
        )
        self.bind_button_action(self.armoff, self.ARM)

    def armonbtn(self):
        self.armonim = PhotoImage(
            file=relative_to_assets("image_20.png"))
        self.armon = self.canvas.create_image(
            1479.0,
            231.0,
            image=self.armonim
        )
        self.bind_button_action(self.armon, self.DISARM)

    def ARM(self):
        command(f'arm("{self.selected_mode}")')
        self.armoffbtn()

    def DISARM(self):
        command(f'disarm("{self.selected_mode}")')
        self.armonbtn()
            
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

    def modeoffbtn2(self):
        command('moder("GUIDED")')
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
        self.bind_button_action(self.modeon, self.modeoffbtn2)
        command(f'moder("{self.selected_mode}")')

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
        command('camera_server()')

    def clawoffbtn(self):
        self.clawoffim = PhotoImage(
            file=relative_to_assets("image_25.png"))
        self.clawoff = self.canvas.create_image(
            1467.0,
            390.0,
            image=self.clawoffim
        )
        self.bind_button_action(self.clawoff, self.clawonbtn)

    def clawoffbtn2(self):
        self.clawoffim = PhotoImage(
            file=relative_to_assets("image_25.png"))
        self.clawoff = self.canvas.create_image(
            1467.0,
            390.0,
            image=self.clawoffim
        )
        self.bind_button_action(self.clawoff, self.clawonbtn)
        command("servo('open')")


    def clawonbtn(self):
        self.clawonim = PhotoImage(
            file=relative_to_assets("image_26.png"))
        self.clawon = self.canvas.create_image(
            1467.0,
            390.0,
            image=self.clawonim
        )
        self.bind_button_action(self.clawon, self.clawoffbtn2)
        command("servo('close')")

    def ctrloffbtn(self):
        self.ctrloffim = PhotoImage(
            file=relative_to_assets("image_27.png"))
        self.ctrloff = self.canvas.create_image(
            1463.0,
            443.0,
            image=self.ctrloffim
        )
        self.bind_button_action(self.ctrloff, self.ctrlonbtn)
        self.canvas.tag_bind(self.ctrloff, '<Button-3>', self.show_ctrl_menu)


        ctrlOFF(self)

    def ctrlonbtn(self):
        self.ctrlonim = PhotoImage(
            file=relative_to_assets("image_28.png"))
        self.ctrlon = self.canvas.create_image(
            1463.0,
            443.0,
            image=self.ctrlonim
        )
        self.bind_button_action(self.ctrlon, self.ctrloffbtn)
        ctrlON(self)

    def tkoffoffbtn(self):
        self.tkoffoffim = PhotoImage(
            file=relative_to_assets("image_29.png"))
        self.tkoffoff = self.canvas.create_image(
            1462.0,
            496.0,
            image=self.tkoffoffim
        )
        self.bind_button_action(self.tkoffoff, self.tkoffonbtn)
        command('land()')

    def tkoffonbtn(self):
        self.tkoffonim = PhotoImage(
            file=relative_to_assets("image_30.png"))
        self.tkoffon = self.canvas.create_image(
            1462.0,
            496.0,
            image=self.tkoffonim
        )
        self.bind_button_action(self.tkoffon, self.tkoffoffbtn)
        command('takeoff()')

    def posoffbtn(self):
        self.posoffim = PhotoImage(
            file=relative_to_assets("image_31.png"))
        self.posoff = self.canvas.create_image(
            1462.0,
            549.0,
            image=self.posoffim
        )
        self.bind_button_action(self.posoff, self.posonbtn)
        command('moder("GUIDED")')

    def posonbtn(self):
        self.posonim = PhotoImage(
            file=relative_to_assets("image_32.png"))
        self.poson = self.canvas.create_image(
            1462.0,
            549.0,
            image=self.posonim
        )
        self.bind_button_action(self.poson, self.posoffbtn)
        command('poshold()')

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
        command('land()')

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
        self.entry_mcu = Entry(self.canvas,
            bd=0,
            bg="#353535",
            fg="#FFFFFF",
            highlightthickness=1,
            highlightbackground="#FFFFFF",  # Set the highlight border color to white
            highlightcolor="#F0FFF0",  # Set the highlight color to white
            font=self.entry_font
        )
        self.entry_mcu.place(
            x=1016.0,
            y=580.0,
            width=336.0,
            height=30.0
        )
        self.entry_mcu.bind('<Return>', lambda event: send(MCU_host,f"{self.entry_mcu.get()}"))
    def cd1entry(self):
        self.entry_cd1_im_im = PhotoImage(
            file=relative_to_assets("image_36.png"))
        self.entry_cd1_im = self.canvas.create_image(
            1184.0,
            527.0,
            image=self.entry_cd1_im_im
        )

        self.entry_cd1_bg = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            1184.0,
            527.0,
            image=self.entry_cd1_bg,
        )
        self.entry_cd1 = Entry(self.canvas,
            bd=0,
            bg="#353535",
            fg="#FFFFFF",
            highlightthickness=1,
            highlightbackground="#FFFFFF",  # Set the highlight border color to white
            highlightcolor="#FF0FFF",
            font=self.entry_font
        )
        self.entry_cd1.place(
            x=1016.0,
            y=511.0,
            width=336.0,
            height=30.0
        )
        self.entry_cd1.bind('<Return>', lambda event: send(CD1_host,f"{self.entry_cd1.get()}"))
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
        self.entry_cd2 = Entry(self.canvas,
            bd=0,
            bg="#353535",
            fg="#FFFFFF",
            highlightthickness=1,
            highlightbackground="#FFFFFF",  # Set the highlight border color to white
            highlightcolor="#00FFFF",
            font=self.entry_font
        )
        self.entry_cd2.place(
            x=1016.0,
            y=442.0,
            width=336.0,
            height=30.0
        )
        self.entry_cd2.bind('<Return>', lambda event: send(CD2_host,f"{self.entry_cd2.get()}"))
 


    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("RoboControllo")
        
        self.current_window = None
        self.ctrl_window = CTRL(self)
        self.miss_window = MISSION(self)
        self.init_window = INIT(self)
        self.edit_window = EDIT(self)

        self.geometry("1500x760+5+0")
        self.configure(bg = "#FFFFFF")
        self.connected_drones = []
        self.selected_mode = "STABILIZE"
        self.control_type = 'send_ned'
        self.entry_font = font.Font(family="Georgia", size=8, weight="normal")
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 760,
            width = 1500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("back.png"))
        self.image_1 = self.canvas.create_image(
            774.0,
            397.0,
            image=self.image_image_1
        )

        self.canvas.place(x = 0, y = 0)

        self.menu = Menu(self.canvas, tearoff=0, font=("Montserrat Bold", 16))

        modes = ["GUIDED", "STABILIZE", "RTL", "BREAK", "LAND", "AUTOTUNE"]
        for mode in modes:
            self.menu.add_command(
                label=mode, command=lambda m=mode: self.set_selected_mode(m))

        self.ctrl_menu = Menu(self.canvas, tearoff=0, font=("Montserrat Bold", 16))

        ctrl_modes = ["send_ned", "ctrl_front"]
        for mode in ctrl_modes:
            self.ctrl_menu.add_command(
                label=mode, command=lambda m=mode: self.ctrl_menu_action(m))

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
            font=self.entry_font,
            bg="#4A4848",
            relief="flat",
            state="disabled"
        )
        self.log_text.place(x=990, y=660, width=510, height=80)
        logger.set_log_text(self.log_text)

        self.log_sec_background = self.canvas.create_rectangle(
            1273.0,
            342.0,
            970.0,
            35.0,
            fill="#000000",
            outline="")

        self.log_text_sec = Text(
            self.canvas,
            wrap="word",
            font=self.entry_font,
            bg="#FFFF00",
            relief="flat",
            state="disabled"
        )
        self.log_text_sec.place(x=971.5, y=39.5, width=300.0, height=300.0)
        logger.set_log_text_sec(self.log_text_sec)

        self.map_background = self.canvas.create_rectangle(
            49.0,
            35.0,
            969.0,
            702.0,
            fill="#442211",
            outline="")
        global add_marker

        add_marker = MapApplication(self)
        add_marker.map_widget.place(x=-240.0, y=-11.0, width=912.0, height=660.0)
        print(add_marker)
        self.armoffbtn()
        self.modeoffbtn()
        self.camoffbtn()
        self.clawoffbtn()
        self.ctrloffbtn()
        self.tkoffoffbtn()
        self.posoffbtn()
        self.landoffbtn()

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

    