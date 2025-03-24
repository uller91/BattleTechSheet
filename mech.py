from tkinter import ttk


def initialize_mech(interface, data):
    mech = {}
    keys = ["HI", "H", "CTI", "CT"]

    h_i = Head_Internal(interface, Point(210,110), data["Internal"]["H"])
    mech[keys[0]] = h_i
    h = Head(interface, Point(200,100), data["Armor"]["H"], h_i)
    mech[keys[1]] = h
    c_t_i = Center_Torso_Internal(interface, Point(210,210), data["Internal"]["C"])
    mech[keys[2]] = c_t_i
    c_t = Center_Torso(interface, Point(200,200), data["Armor"]["C"], c_t_i)
    mech[keys[3]] = c_t
    #print(mech)
    
    
    #drawing mech part in reverse order to have proper layers position
    keys.reverse()
    for key in keys:
        mech[key].draw()

    return mech


class Point(): #legacy code from window. Can be deleted/rewritten in the Mech class?
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


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

        #self.draw()

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


class Head(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        coordinates = [0,0, 50,0, 50,90, 0,90]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i] + self._x)
            else:
                used_coordinates.append(coordinates[i] + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[3] + used_coordinates[5] - 2*coordinates[5])/2 
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}")

class Head_Internal(Head):
    def __init__(self, interface, coordinates, stat, child = None):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        coordinates = [0,0, 30,0, 30,70, 0,70]
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
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}")


class Center_Torso(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        coordinates = [0,0, 50,0, 50,90, 0,90]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i] + self._x)
            else:
                used_coordinates.append(coordinates[i] + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[3] + used_coordinates[5] + 2*coordinates[5])/2 
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}")

class Center_Torso_Internal(Center_Torso):
    def __init__(self, interface, coordinates, stat, child = None):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        coordinates = [0,0, 30,0, 30,70, 0,70]
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
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}")