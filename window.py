import random

from tkinter import Tk, Canvas, StringVar
from tkinter import ttk

from read_data import read_mech_list, read_mech_data
from mech import initialize_mech


class Interface():
    def __init__(self, win):
        self._w = win
        self._root = win._root
        self._mech = []
        self._mech_list = read_mech_list()
        self._mech_data = []

        #initiating the Canvas - need to move mech drawing/creation after the mech is chosen
        self._canvas = Canvas(self._root, width=600, height=600)

        # initiating the original window with the mech select
        self._frame = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=300, height=200)
        self._frame.grid(column=0, row=0, columnspan=3, rowspan=2)

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


    def initiate_the_rest_of_the_grid(self):
        self._mech_label = ttk.Label(self._frame, text="")
        self._mech_label.place(x=10, y=19)

        #drawing the canvas
        self._canvas.grid(column=3, row=0, columnspan=1, rowspan=4)

        self._frame_2 = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=300, height=200)
        self._frame_2.grid(column=0, row=2, columnspan=3, rowspan=2)
        
        self._button_3 = ttk.Button(self._frame_2, text="Do 5 damage", command=self.do_5_damage)
        self._button_3.place(x=10, y=10)
        self._button_4 = ttk.Button(self._frame_2, text="Do 20 damage", command=self.do_20_damage)
        self._button_4.place(x=10, y=50)


    def do_5_damage(self):
        part = self.get_random_part()
        self._mech[part].damage(5)

    def do_20_damage(self):
        part = self.get_random_part()
        self._mech[part].damage(20)

    def get_random_part(self):
        value = random.randint(1,6) + random.randint(1,6)
        part = "H"
        if value == 2 or value == 7:
            part = "CT"
        elif value == 3 or value == 4:
            part = "RA"
        elif value == 5:
            #part = "RL"
            part = "RA"
        elif value == 6:
            part = "RT"
        elif value == 8:
            part = "LT"
        elif value == 9:
            #part = "LL"
            part = "LA"
        elif value == 10 or value == 11:
            part = "LA"
        else:
            part = "H"
        return part



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
        self._frame["height"] = 100
        self._mech_label["text"] = self._mech_data["Variant"] + " - " + self._mech_data["Model"]
        self.initialize_the_mech() 


    def initialize_the_mech(self):
        self._mech = initialize_mech(self, self._mech_data, 300, 300)     # (300, 300) - center of the Canvas
    
        


class Window():
    def __init__(self, width, height, title = "BattleTech Interactable Sheet"):
        self._root = Tk()
        self._root.title(title)
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._mech = None
        
    def close(self):
        print("The program is closed.")
        self._root.quit()
    
    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

#things below may be not needed
class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)