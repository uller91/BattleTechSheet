from tkinter import Tk
from tkinter import ttk


class Window():
    def __init__(self, width, height, title = "BattleTech Interactable Sheet"):
        self._root = Tk()
        self._root.title(title)
        #self.__canvas = Canvas(self.__root, bg="grey", height=height, width=width)
        #self.__canvas.pack(fill=BOTH, expand=1)
        self._content = ttk.Frame(self._root)
        #self._is_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.add_objects()
        self._root.mainloop()
        
    #def redraw(self):
    #    self._root.update_idletasks()
    #    self._root.update()

    #def wait_for_close(self):
    #    self._is_running = True
    #    while self._is_running:
    #        self.redraw()
    #    print("The program is closed.")

    def close(self):
        #self._is_running = False
        self._root.quit()

    def add_objects(self):
        self._frame = ttk.Frame(self._content, borderwidth=5, relief="ridge", width=200, height=100)
        self._frame_2 = ttk.Frame(self._content, borderwidth=5, relief="ridge", width=200, height=100)
        self._namelbl = ttk.Label(self._content, text="Name")
        self._surnamelbl = ttk.Label(self._content, text="Surname")
        
        self.initiate_the_grid()

    def initiate_the_grid(self):
        self._content.grid(column=0, row=0)

        self._frame.grid(column=0, row=0, columnspan=3, rowspan=2)
        self._frame_2.grid(column=0, row=2, columnspan=3, rowspan=2)
        self._namelbl.grid(column=0, row=0, columnspan=2)
        self._surnamelbl.grid(column=0, row=1, columnspan=2)