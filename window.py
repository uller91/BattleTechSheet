import os

from tkinter import *
from tkinter import ttk

from read_data import read_mech_list, read_mech_data
from mech import initialize_mech
from components import initialize_components
from get_random import get_random_part, get_random_position


class Interface():
    def __init__(self, win):
        self._w = win
        self._root = win._root
        self._mech = {}
        self._mech_list = read_mech_list()
        self._mech_data = []
        self._components = {}

        self._engine_hit = 0
        self._gyro_hit = 0
        self._sensor_hit = 0
        self._life_support = 0

        #window geometry
        #self._root.geometry(f'{win._width}x{win._height}+100+100') 
        self._root.geometry('+100+100')

        # initiating the original window with the mech select and the first frame
        self._frame = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=350, height=200)
        self._frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky="NW")

        #version
        self.version = ttk.Label(self._frame, text="v. 0.1", font=("arial", 7, "normal"))
        self.version.place(x=305, y=175)

        self.mech_variant = StringVar() #self is needed to .current to work. Otherwise it will be garbage collected and the combobox will start empty
        self.mechs_variants = list(self._mech_list.keys())
        self._list_variant = ttk.Combobox(self._frame, textvariable=self.mech_variant, values=self.mechs_variants, state="readonly", height=5)
        self._list_variant.current(0)
        self._list_variant.place(x=10, y=50)
        
        self._button = ttk.Button(self._frame, text="Choose Mech Model", command=self.choose_mech_variant)
        self._button.place(x=10, y=10)

        self.mech_model = StringVar()
        self._list_model = ttk.Combobox(self._frame, textvariable=self.mech_model, state="disabled", height=5)
        self._list_model.place(x=10, y=130)

        self._button_2 = ttk.Button(self._frame, text="Choose Mech Variant", command=self.choose_mech_model, state="disabled")
        self._button_2.place(x=10, y=90)


    def choose_mech_variant(self):
        self._button["state"] = "disabled"
        self._list_variant["state"] = "disabled"

        self._button_2["state"] = "enabled"
        self._list_model["state"] = "readonly"

        self._list_model["values"] = list(self._mech_list[self._list_variant.get()].keys())
        self._list_model.current(0)


    def choose_mech_model(self):
        self._button.place_forget()
        self._list_variant.place_forget()
        self._button_2.place_forget()
        self._list_model.place_forget()

        self._mech_data = read_mech_data(self._mech_list[self._list_variant.get()][self._list_model.get()], self._list_variant.get(), self._list_model.get())

        self.initiate_the_rest_of_the_grid()
        #self._frame["height"] = 200
        self._mech_label["text"] = self._mech_data["Variant"] + " - " + self._mech_data["Model"]

        self.initialize_the_components()
        self.initialize_the_mech(self._components)
        


    def initiate_the_rest_of_the_grid(self):
        #drawing the first frame
        self._mech_label = ttk.Label(self._frame, text="")
        self._mech_label.place(x=10, y=20)
        self._mech_label_2 = ttk.Label(self._frame, text=f"Tonnage: {self._mech_data["Tonnage"]}")
        self._mech_label_2.place(x=10, y=60)
        self._mech_label_3 = ttk.Label(self._frame, text=f"Heat Sinks: {self._mech_data["Heat Sink"]}")
        self._mech_label_3.place(x=10, y=80)
        self._mech_label_4 = ttk.Label(self._frame, text=f"BV: {self._mech_data["BV"]}")
        self._mech_label_4.place(x=10, y=100)
        self._mech_label_5 = ttk.Label(self._frame, text=f"Movement Points:\nWalking:{self._mech_data["Speed"]["W"]}, Running:{self._mech_data["Speed"]["R"]}, Jumping:{self._mech_data["Speed"]["J"]}")
        self._mech_label_5.place(x=10, y=140)

        #drawing the canvas
        self._canvas = Canvas(self._root, width=400, height=700)
        self._canvas.grid(column=4, row=0, columnspan=1, rowspan=6)

        #drawing the second frame
        self._frame_2 = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=350, height=200)
        self._frame_2.grid(column=2, row=0, columnspan=2, rowspan=2, sticky="NW")
        
        self._button_3 = ttk.Button(self._frame_2, text="Do 5 damage", command=self.do_5_damage)
        self._button_3.place(x=220, y=80)
        self._button_4 = ttk.Button(self._frame_2, text="Do 20 damage", command=self.do_20_damage)
        self._button_4.place(x=220, y=110)
        self._button_6 = ttk.Button(self._frame_2, text="Left Torso Crit!", command=self.destroy_ammo)
        self._button_6.place(x=10, y=90)
        self._button_7 = ttk.Button(self._frame_2, text="Hit Internal Center Torso!", command=self.hit_center)
        self._button_7.place(x=10, y=120)
        self._button_8 = ttk.Button(self._frame_2, text="Shoot Criticals Through Armor!", command=self.through_crit)
        self._button_8.place(x=10, y=150)

        self._button_5 = ttk.Button(self._frame_2, text="Restart", command=self.restart)
        self._button_5.place(x=240, y=150)

        self.attack_position = StringVar()
        
        self._radio_1 = ttk.Radiobutton(self._frame_2, text="Front", variable=self.attack_position, value="front")
        self._radio_1.place(x=10, y=10)
        self._radio_2 = ttk.Radiobutton(self._frame_2, text="Rear", variable=self.attack_position, value="rear")
        self._radio_2.place(x=70, y=10)
        self._radio_3 = ttk.Radiobutton(self._frame_2, text="Left", variable=self.attack_position, value="left")
        self._radio_3.place(x=130, y=10)
        self._radio_4 = ttk.Radiobutton(self._frame_2, text="Right", variable=self.attack_position, value="right")
        self._radio_4.place(x=190, y=10)
        self._radio_1 = ttk.Radiobutton(self._frame_2, text="Random location", variable=self.attack_position, value="random")
        self._radio_1.place(x=10, y=50)
        self.attack_position.set("random")

        #drawing the second canvas
        self._canvas_2 = Canvas(self._root, width=700, height=500)
        self._canvas_2.grid(column=0, row=2, columnspan=4, rowspan=4, sticky="NW")
        

    def initialize_the_mech(self, components):
        self._mech = initialize_mech(self, self._mech_data, components, 175, 350)     # (300, 300) - center of the Canvas

        keys = ["HI", "CTI", "LTI", "RTI", "LAI", "RAI", "LLI", "RLI"]
        for key in keys:
            self._components[key]._part = self._mech[key]


    def initialize_the_components(self):
        self._components = initialize_components(self, self._mech_data, 350, 50)


    def do_5_damage(self):
        self.do_x_damage(5)

    def do_20_damage(self):
        self.do_x_damage(20)

    def do_x_damage(self, value):
        if self.attack_position.get() == "random":
            location = get_random_position()
        else:
            location = self.attack_position.get()
        part = get_random_part(location)

        if part == "CRIT":
            match location:
                case "front":
                    self._mech["CT"].damage(value, through = True)
                case "rear":
                    self._mech["RCT"].damage(value, through = True)
                case "left":
                    self._mech["LT"].damage(value, through = True)
                case "rigt":
                    self._mech["RT"].damage(value, through = True)
        else:
            self._mech[part].damage(value)

        if self._engine_hit >= 3:
            print("!!! Mech is destroyed by engine explosion !!!")


    def destroy_ammo(self):
        self._components["LTI"].damage(1)
        

    def hit_center(self):
        self._mech["CTI"].damage(1)
        if self._engine_hit >= 3:
            print("!!! Mech is destroyed by engine explosion !!!")


    def through_crit(self):
        if self.attack_position.get() == "random":
            location = get_random_position()
        else:
            location = self.attack_position.get()

        match location:
            case "front":
                self._mech["CT"].damage(1, through = True)
            case "rear":
                self._mech["RCT"].damage(1, through = True)
            case "left":
                self._mech["LT"].damage(1, through = True)
            case "rigt":
                self._mech["RT"].damage(1, through = True)

        if self._engine_hit >= 3:
            print("!!! Mech is destroyed by engine explosion !!!")


    def restart(self):
        frame = Frame(self._root)
        for widget in frame.winfo_children():
            widget.destroy()
        self._root.destroy()
        
        win = Window(1280, 720)
        interface = Interface(win)



class Window():
    def __init__(self, width, height, title = "BattleTech Interactable Sheet"):
        self._root = Tk()
        self._root.title(title)
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._mech = None
        self._width = width
        self._height = height
        
        
    def close(self):
        print("The program is closed.")
        self._root.quit()
