from tkinter import Tk, Canvas, StringVar
from tkinter import ttk


class Interface():
    def __init__(self, win):
        self._w = win
        self._root = win._root
        self._mech = None
        
        self._canvas = Canvas(self._root, width=600, height=600)
        self._frame = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=300, height=100)
        self._frame_2 = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=300, height=200)
        #self._namelbl = ttk.Label(self._root, text="Name")
        #self._surnamelbl = ttk.Label(self._root, text="Surname")
        self._button = ttk.Button(self._frame_2, text="okay", command=self.do_stuff)
        self._button_2 = ttk.Button(self._frame_2, text="not okay", command=self.do_bad_stuff)

        self.mech = StringVar() #self is needed to .current to work. Otherwise it will be garbage collected and the combobox will start empty
        self.mechs_variants = ["a", "b", "c", "d", "e", "f", "g"]
        self._list = ttk.Combobox(self._frame, textvariable=self.mech, values=self.mechs_variants, state="readonly", height=5)
        self._list.current(0)
        self._button_3 = ttk.Button(self._frame, text="choose mech", command=self.choose_mech)
        self._mech_label = ttk.Label(self._frame, text="")

        self.initiate_the_grid()

    def initiate_the_grid(self):
        self._frame.grid(column=0, row=0, columnspan=3, rowspan=2)
        #self._namelbl.grid(column=0, row=0, columnspan=2)
        #self._surnamelbl.grid(column=0, row=1, columnspan=2)

        self._list.place(x=10, y=50)
        self._button_3.place(x=10, y=10)

    def initiate_the_rest_of_the_grid(self):
        self._canvas.grid(column=3, row=0, columnspan=1, rowspan=4)
        self._frame_2.grid(column=0, row=2, columnspan=3, rowspan=2)
        self._button.place(x=10, y=10)
        self._button_2.place(x=10, y=50)

    def do_stuff(self):
        #if self._list.get() == "a":
        #    print("bonk")
        self._mech.damage(5)

    def do_bad_stuff(self):
        self._mech.damage(20)

    def choose_mech(self):
        self._list["state"] = "disabled"
        #self._button_3["text"] = self._list.get()
        self._button_3.place_forget()
        self._list.place_forget()
        self.initiate_the_rest_of_the_grid()
        self._mech_label["text"] = self._list.get() + "!!!"
        self._mech_label.place(x=10, y=19)