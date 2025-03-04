from tkinter import Tk, BOTH, Canvas
from tkinter import ttk


class Window():
    def __init__(self, width, height, title = "BattleTech Interactable Sheet"):
        self.__root = Tk()
        self.__root.title(title)
        self.__canvas = Canvas(self.__root, bg="grey", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("The program is closed.")

    def close(self):
        self.__is_running = False
