from tkinter import Tk, Canvas
from tkinter import ttk


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