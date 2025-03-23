from tkinter import ttk


class Mech():
    def __init__(self, interface, coordinates, stat, child, fill_color = "white", outline_color = "green"):
        self._i = interface
        self._x = coordinates.x
        self._y = coordinates.y
        self._stat = int(stat)
        self._damage = 0
        self._destroyed = False
        self._polygon = None
        self._fill = fill_color
        self._outline = outline_color
        self._child = child

        self.draw()

    def draw(self):
        pass

    def damage(self, damage):
        self._damage += damage
        damage_spill = 0
        if self._damage < self._stat:
            self._i._canvas.itemconfig(self._polygon, fill="white", outline="green", width = 3)
        else:
            self._destroyed = True
            self._i._canvas.itemconfig(self._polygon, fill="red", outline="black", width = 1)
            damage_spill = self._damage - self._stat
            self._damage -= damage_spill
            if self._child == None:
                print("Mech is destroyed!")
            elif self._child != None:
                self._child.damage(damage_spill)
        
        self._i._canvas.itemconfig(self._text, text=f"{self._damage}\n/\n{self._stat}")


class Center_Torso(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        coordinates = [0,0, 40,0, 40,80, 0,80]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i] + self._x)
            else:
                used_coordinates.append(coordinates[i] + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[3] + used_coordinates[5])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}") #coordinates?

class Inner_Center_Torso(Center_Torso):
    def __init__(self, interface, coordinates, stat, child = None):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        coordinates = [0,0, 40,0, 40,80, 0,80]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i] + self._x)
            else:
                used_coordinates.append(coordinates[i] + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[3] + used_coordinates[5])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}") #coordinates?