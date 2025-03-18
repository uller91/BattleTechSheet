from window import Line, Point
from tkinter import ttk

class Mech():
    def __init__(self, interface, coordinates):
        self._w = interface
        self._x = coordinates.x
        self._y = coordinates.y
        self.center_torso = True
        #print("prepared")
        
        self.draw_center_torso("green")

    def draw_center_torso(self, fill_color):
        self.size_x = 200
        self.size_y = 200
        offset = f"#{self.size_x},{self.size_y}"
        coordinates = [0,0, 100,0, 100,200, 0,200]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i] + self.size_x)
            else:
                used_coordinates.append(coordinates[i] + self.size_y)
        self._rect = self._w._canvas.create_polygon(used_coordinates, fill="white", outline=fill_color, width = 3)
        self._text = self._w._canvas.create_text(250,300, anchor="center", justify="center", text=f"{self._w.variable}\n/\n20")

