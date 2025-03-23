from tkinter import Tk, Canvas, StringVar
from tkinter import ttk

from read_data import read_mech_list, read_mech_data
from mech import Center_Torso, Inner_Center_Torso


class Interface():
    def __init__(self, win):
        self._w = win
        self._root = win._root
        self._mech = None
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
        
        self._button_3 = ttk.Button(self._frame_2, text="okay", command=self.do_stuff)
        self._button_3.place(x=10, y=10)
        self._button_4 = ttk.Button(self._frame_2, text="not okay", command=self.do_bad_stuff)
        self._button_4.place(x=10, y=50)


    def do_stuff(self):
        self._mech.damage(5)

    def do_bad_stuff(self):
        self._mech.damage(20)


    def choose_mech_variant(self):
        self._button["state"] = "disabled"
        self._list_variant["state"] = "disabled"

        self._button_2["state"] = "enabled"
        self._list_model["state"] = "readonly"

        self._list_model["values"] = self._mech_list[self._list_variant.get()]
        self._list_model.current(0)


    def choose_mech_model(self):
        self._button.place_forget()
        self._list_variant.place_forget()
        self._button_2.place_forget()
        self._list_model.place_forget()

        self._mech_data = read_mech_data(self._list_variant.get(), self._list_model.get())

        self.initiate_the_rest_of_the_grid()
        self._frame["height"] = 100
        self._mech_label["text"] = self._mech_data[0] + " - " + self._mech_data[1]
        self.initialize_the_mech() #continue here


    def initialize_the_mech(self):
        i_c_t = Inner_Center_Torso(self, Point(100,350), self._mech_data[22])
        c_t = Center_Torso(self, Point(100,100), self._mech_data[11], i_c_t)
    
        self._mech = c_t


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