from tkinter import Tk, Canvas
from tkinter import ttk


class Interface():
    def __init__(self, win):
        self._w = win
        self._root = win._root
        self._mech = None

        self.variable = 0
        
        self._canvas = Canvas(self._root, width=600, height=600)
        self._frame = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=200, height=200)
        self._frame_2 = ttk.Frame(self._root, borderwidth=5, relief="ridge", width=200, height=100)
        self._namelbl = ttk.Label(self._root, text="Name")
        self._surnamelbl = ttk.Label(self._root, text="Surname")
        self._button = ttk.Button(self._frame, text="okay", command=self.do_stuff)
        self._button_2 = ttk.Button(self._frame_2, text="not okay", command=self.do_bad_stuff)
        
        self.initiate_the_grid()

    def initiate_the_grid(self):
        self._frame.grid(column=0, row=0, columnspan=3, rowspan=2)
        self._frame_2.grid(column=0, row=2, columnspan=3, rowspan=2)
        self._namelbl.grid(column=0, row=0, columnspan=2)
        self._surnamelbl.grid(column=0, row=1, columnspan=2)
        self._button.place(x=10, y=30)
        self._button_2.place(x=10, y=10)
        self._canvas.grid(column=3, row=0, columnspan=1, rowspan=4)

    def do_stuff(self):
        self._canvas.itemconfig(self._mech._rect, fill="white", outline="green", width = 3)
        self.variable += 1
        if self.variable < 20:
            self._canvas.itemconfig(self._mech._text, text=f"{self.variable}\n/\n20")
        else:
            self._canvas.itemconfig(self._mech._text, text=f"{self.variable}\n/\n20")
            self.do_bad_stuff()
        #print(self.variable)
        print("okay!")

    #move to interface
    def do_bad_stuff(self):
        self._canvas.itemconfig(self._mech._rect, fill="red", outline="black", width = 1)
        print("not okay!")