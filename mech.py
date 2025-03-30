from tkinter import ttk


def initialize_mech(interface, data, x0, y0):
    mech = {}
    keys = ["HI", "H", "CTI", "CT", "LTI", "LT", "RTI", "RT", "LAI", "LA", "RAI", "RA", "LLI", "LL", "RLI", "RL"]

    h_i = Mech(interface, keys[0], Point(x0,y0-225), data["Internal"]["H"], [0,0, 1,0, 1,2, 0,2], None, [40, 30], [0,2,3,5], inner = True)
    mech[keys[0]] = h_i
    h = Mech(interface, keys[1], Point(x0,y0-225), data["Armor"]["H"], [0,0, 1,0, 1,2, 0,2], h_i, [40, 30], [0,2,3,5], off_y = -1.8, fill_color="", outline_color="green")
    mech[keys[1]] = h
    c_t_i = Mech(interface, keys[2], Point(x0-5,y0-160), data["Internal"]["C"], [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2], None, [25, 20], [0,2,1,13], inner = True)
    mech[keys[2]] = c_t_i
    c_t = Mech(interface, keys[3], Point(x0-5,y0-160), data["Armor"]["C"], [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2], c_t_i, [25, 20], [0,2,1,13], off_y = 4.8, fill_color="", outline_color="green")
    mech[keys[3]] = c_t

    l_t_i = Mech(interface, keys[4], Point(x0-48,y0-160), data["Internal"]["T"], [-1,0, 1.5,0, 1.5,1, 0.5,1, 0.5,2, -1,2], c_t, [25, 35], [0,6,1,9], inner = True)
    mech[keys[4]] = l_t_i
    l_t = Mech(interface, keys[5], Point(x0-48,y0-160), data["Armor"]["T"], [-1,0, 1.5,0, 1.5,1, 0.5,1, 0.5,2, -1,2], l_t_i, [25, 35], [0,6,1,9], off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[5]] = l_t
    r_t_i = Mech(interface, keys[6], Point(x0+75,y0-160), data["Internal"]["T"], [-1,0, 1.5,0, 1.5,2, 0,2, 0,1, -1,1], c_t, [25, 35], [6,4,3,5], inner = True)
    mech[keys[6]] = r_t_i
    r_t = Mech(interface, keys[7], Point(x0+75,y0-160), data["Armor"]["T"], [-1,0, 1.5,0, 1.5,2, 0,2, 0,1, -1,1], r_t_i, [25, 35], [6,4,3,5], off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[7]] = r_t

    l_a_i = Mech(interface, keys[8], Point(x0-103,y0-160), data["Internal"]["A"], [0,0, 1,0, 1,2, 0,3, 0,4, 1,4, 1,5, -1,5, -1,1], l_t, [25, 25], [0,0,3,7], inner = True)
    mech[keys[8]] = l_a_i
    l_a = Mech(interface, keys[9], Point(x0-103,y0-160), data["Armor"]["A"], [0,0, 1,0, 1,2, 0,3, 0,4, 1,4, 1,5, -1,5, -1,1], l_a_i, [25, 25], [0,0,3,7], off_x = -1, off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[9]] = l_a
    r_a_i = Mech(interface, keys[10], Point(x0+143,y0-160), data["Internal"]["A"], [0,0, -1,0, -1,2, 0,3, 0,4, -1,4, -1,5, 1,5, 1,1], r_t, [25, 25], [0,0,3,7], inner = True)
    mech[keys[10]] = r_a_i
    r_a = Mech(interface, keys[11], Point(x0+143,y0-160), data["Armor"]["A"], [0,0, -1,0, -1,2, 0,3, 0,4, -1,4, -1,5, 1,5, 1,1], r_a_i, [25, 25], [0,0,3,7], off_x = 1, off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[11]] = r_a

    l_l_i = Mech(interface, keys[12], Point(x0-10,y0-55), data["Internal"]["L"], [0,0, 0,7, 1,8, 1,9, -4,9, -4,8, -3,7, -3,1, -2,0], l_t, [15, 15], [2,14,3,15], inner = True)
    mech[keys[12]] = l_l_i
    l_l = Mech(interface, keys[13], Point(x0-10,y0-55), data["Armor"]["L"], [0,0, 0,7, 1,8, 1,9, -4,9, -4,8, -3,7, -3,1, -2,0], l_l_i, [15, 15], [2,14,3,15], off_x = -2.3, fill_color="", outline_color="green")
    mech[keys[13]] = l_l
    r_l_i = Mech(interface, keys[14], Point(x0+50,y0-55), data["Internal"]["L"], [0,0, 0,7, -1,8, -1,9, 4,9, 4,8, 3,7, 3,1, 2,0], r_t, [15, 15], [2,14,3,15], inner = True)
    mech[keys[14]] = r_l_i
    r_l = Mech(interface, keys[15], Point(x0+50,y0-55), data["Armor"]["L"], [0,0, 0,7, -1,8, -1,9, 4,9, 4,8, 3,7, 3,1, 2,0], r_l_i, [15, 15], [2,14,3,15], off_x = 2.3, fill_color="", outline_color="green")
    mech[keys[15]] = r_l


    for key in keys:
        mech[key].draw()

    return mech


class Point(): #legacy code from window. Can be deleted/rewritten in the Mech class?
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Mech():
    def __init__(self, interface, name, coordinates, stat, polygon, child, scale, text, off_x = 0, off_y = 0, inner = False, fill_color = "pale green", outline_color = "red"):
        self._i = interface
        self._name = name
        self._x = coordinates.x
        self._y = coordinates.y
        self._stat = int(stat)
        self._polygon = polygon
        self._damage = 0
        self._destroyed = False
        self._inner = inner
        self._fill = fill_color
        self._outline = outline_color
        self._child = child
        self._scale_x = scale[0]
        self._scale_y = scale[1]
        self._text_centre = text
        self._off_x = off_x
        self._off_y = off_y


    def draw(self):
        used_coordinates = []
        for i in range(len(self._polygon)):
            if i%2 == 0:
                used_coordinates.append(self._polygon[i]*self._scale_x + self._x)
            else:
                used_coordinates.append(self._polygon[i]*self._scale_y + self._y)
        center_x = (used_coordinates[self._text_centre[0]] + used_coordinates[self._text_centre[1]])/2 + self._off_x*self._scale_x
        center_y = (used_coordinates[self._text_centre[2]] + used_coordinates[self._text_centre[3]])/2 + self._off_y*self._scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        if self._inner == False:
            self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))
        else:
            self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",7, "normal"))

    def damage(self, damage):
        self._damage += damage
        damage_spill = 0
        if self._damage < self._stat:
            #self._i._canvas.itemconfig(self._polygon, outline="green", width = 3)
            pass
        else:
            if self._destroyed == False:
                print(f"{self._name} is destroyed!")
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
                self._i._canvas.itemconfig(self._text, font=("arial",7, "normal"))
                self._child._i._canvas.itemconfig(self._child._text, font=("arial",9, "bold"))
                self._child.damage(damage_spill)
        
        self._i._canvas.itemconfig(self._text, text=f"{self._damage}\n/\n{self._stat}")