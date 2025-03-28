from tkinter import ttk


def initialize_mech(interface, data, x0, y0):
    mech = {}
    keys = ["HI", "H", "CTI", "CT", "LTI", "LT", "RTI", "RT", "LAI", "LA", "RAI", "RA"]

    h_i = Head_Internal(interface, Point(x0,y0/4), data["Internal"]["H"])
    mech[keys[0]] = h_i
    h = Head(interface, Point(x0,y0/4), data["Armor"]["H"], h_i)
    mech[keys[1]] = h
    c_t_i = Center_Torso_Internal(interface, Point(x0-5,y0/2-10), data["Internal"]["C"])
    mech[keys[2]] = c_t_i
    c_t = Center_Torso(interface, Point(x0-5,y0/2-10), data["Armor"]["C"], c_t_i)
    mech[keys[3]] = c_t

    l_t_i = Left_Torso_Internal(interface, Point(x0-60,y0/2-10), data["Internal"]["T"], c_t)
    mech[keys[4]] = l_t_i
    l_t = Left_Torso(interface, Point(x0-60,y0/2-10), data["Armor"]["T"], l_t_i)
    mech[keys[5]] = l_t
    r_t_i = Right_Torso_Internal(interface, Point(x0+75,y0/2-10), data["Internal"]["T"], c_t)
    mech[keys[6]] = r_t_i
    r_t = Right_Torso(interface, Point(x0+75,y0/2-10), data["Armor"]["T"], r_t_i)
    mech[keys[7]] = r_t

    l_a_i = Left_Arm_Internal(interface, Point(x0-115,y0/2-10), data["Internal"]["A"], l_t)
    mech[keys[8]] = l_a_i
    l_a = Left_Arm(interface, Point(x0-115,y0/2-10), data["Armor"]["A"], l_a_i)
    mech[keys[9]] = l_a
    r_a_i = Right_Arm_Internal(interface, Point(x0+155,y0/2-10), data["Internal"]["A"], r_t)
    mech[keys[10]] = r_a_i
    r_a = Right_Arm(interface, Point(x0+155,y0/2-10), data["Armor"]["A"], r_a_i)
    mech[keys[11]] = r_a

    
    #TO DO:
    #LL and RL (dont forget to chage random)
    #do one draw fucntion for everything: pass coordinates, scale, text move constants and part name for the log
    #colapse all the classe into one "part" class
    

    for key in keys:
        mech[key].draw()

    return mech


class Point(): #legacy code from window. Can be deleted/rewritten in the Mech class?
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Mech():
    def __init__(self, interface, coordinates, stat, child, fill_color = "pale green", outline_color = "red"):
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
            #self._i._canvas.itemconfig(self._polygon, outline="green", width = 3)
            pass
        else:
            self._destroyed = True
            if self._i._canvas.itemcget(self._polygon,'fill') == "":
                #self._i._canvas.itemconfig(self._polygon, outline="red", width = 3)
                self._i._canvas.delete(self._polygon)
            else:
                self._i._canvas.itemconfig(self._polygon, fill="red", outline="black", width = 3)
            damage_spill = self._damage - self._stat
            self._damage -= damage_spill
            if self._child == None:
                print("Mech is destroyed!")
            elif self._child != None:
                self._i._canvas.itemconfig(self._text, font=("arial",9, "normal"))
                self._child._i._canvas.itemconfig(self._child._text, font=("arial",9, "bold"))
                self._child.damage(damage_spill)
        
        self._i._canvas.itemconfig(self._text, text=f"{self._damage}\n/\n{self._stat}")


class Head(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 40
        scale_y = 30
        coordinates = [0,0, 1,0, 1,2, 0,2]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[3] + used_coordinates[5])/2 - 1.8*scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill="", outline="green", width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))

class Head_Internal(Head):
    def __init__(self, interface, coordinates, stat, child = None):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 40
        scale_y = 30
        coordinates = [0,0, 1,0, 1,2, 0,2]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[3] + used_coordinates[5])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9))


class Center_Torso(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 20
        coordinates = [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[1] + used_coordinates[13])/2 + 4.8*scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill="", outline="green", width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))

class Center_Torso_Internal(Center_Torso):
    def __init__(self, interface, coordinates, stat, child = None):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 20

        coordinates = [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[2])/2
        center_y = (used_coordinates[1] + used_coordinates[13])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9))


class Left_Torso(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 35

        coordinates = [-1,0, 2,0, 2,1, 1,1, 1,2, -1,2]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[6])/2
        center_y = (used_coordinates[1] + used_coordinates[7])/2 - 1.2*scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill="", outline="green", width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))

class Left_Torso_Internal(Left_Torso):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 35
        coordinates = [-1,0, 2,0, 2,1, 1,1, 1,2, -1,2]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[6])/2
        center_y = (used_coordinates[1] + used_coordinates[9])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9))\
        

class Right_Torso(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 35
        coordinates = [-1,0, 2,0, 2,2, 0,2, 0,1, -1,1]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[6] + used_coordinates[4])/2
        center_y = (used_coordinates[3] + used_coordinates[5])/2 - 1.7*scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill="", outline="green", width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))

class Right_Torso_Internal(Right_Torso):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 35
        coordinates = [-1,0, 2,0, 2,2, 0,2, 0,1, -1,1]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[6] + used_coordinates[4])/2
        center_y = (used_coordinates[3] + used_coordinates[5])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9))


class Left_Arm(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 30
        coordinates = [0,0, 1,0, 1,2, 0,3, 0,4, 1,4, 1,5, -1,5, -1,1]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[0])/2 - 1*scale_x
        center_y = (used_coordinates[3] + used_coordinates[7])/2 - 1.7*scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill="", outline="green", width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))

class Left_Arm_Internal(Left_Arm):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 30
        coordinates = [0,0, 1,0, 1,2, 0,3, 0,4, 1,4, 1,5, -1,5, -1,1]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[0])/2
        center_y = (used_coordinates[3] + used_coordinates[7])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9))


class Right_Arm(Mech):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 30
        coordinates = [0,0, -1,0, -1,2, 0,3, 0,4, -1,4, -1,5, 1,5, 1,1]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[0])/2 + 1*scale_x
        center_y = (used_coordinates[3] + used_coordinates[7])/2 - 1.7*scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill="", outline="green", width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))

class Right_Arm_Internal(Right_Arm):
    def __init__(self, interface, coordinates, stat, child):
        super().__init__(interface, coordinates, stat, child)

    def draw(self):
        scale_x = 25
        scale_y = 30
        coordinates = [0,0, -1,0, -1,2, 0,3, 0,4, -1,4, -1,5, 1,5, 1,1]
        used_coordinates = []
        for i in range(len(coordinates)):
            if i%2 == 0:
                used_coordinates.append(coordinates[i]*scale_x + self._x)
            else:
                used_coordinates.append(coordinates[i]*scale_y + self._y)
        #print(used_coordinates)
        center_x = (used_coordinates[0] + used_coordinates[0])/2
        center_y = (used_coordinates[3] + used_coordinates[7])/2
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9))