from get_random import get_random_crit


def initialize_mech(interface, data, components, x0, y0):
    mech = {}
    names = ["Head", "Head Armor", "Cetner Torso", "Center Torso Armor", "Left Torso", "Left Torso Armor", "Right Torso", "Right Torso Armor", "Left Arm", "Left Arm Armor", "Right Arm", "Right Arm Armor", "Left Leg", "Left Leg Armor", "Right Leg", "Right Leg Armor", "Rear Center Torso Armor", "Rear Left Torso Armor", "Rear Right Torso Armor"]
    keys = ["HI", "H", "CTI", "CT", "LTI", "LT", "RTI", "RT", "LAI", "LA", "RAI", "RA", "LLI", "LL", "RLI", "RL", "RCT", "RLT", "RRT"]

    h_i = Mech(interface, names[0], keys[0], [x0,y0-225], data["Internal"]["H"], components[keys[0]], [0,0, 1,0, 1,2, 0,2], None, [40, 30], [0,2,3,5], inner = True)
    mech[keys[0]] = h_i
    h = Mech(interface, names[1], keys[1], [x0,y0-225], data["Armor"]["H"], None, [0,0, 1,0, 1,2, 0,2], h_i, [40, 30], [0,2,3,5], off_y = -1.8, fill_color="", outline_color="green")
    mech[keys[1]] = h
    c_t_i = Mech(interface, names[2], keys[2], [x0-5,y0-160], data["Internal"]["C"], components[keys[2]], [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2], None, [25, 20], [0,2,1,13], inner = True)
    mech[keys[2]] = c_t_i
    c_t = Mech(interface, names[3], keys[3], [x0-5,y0-160], data["Armor"]["C"], None, [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2], c_t_i, [25, 20], [0,2,1,13], off_y = 4.8, fill_color="", outline_color="green")
    mech[keys[3]] = c_t

    l_t_i = Mech(interface, names[4], keys[4], [x0-48,y0-160], data["Internal"]["T"], components[keys[4]], [-1,0, 1.5,0, 1.5,1, 0.5,1, 0.5,2, -1,2], c_t, [25, 35], [0,6,1,9], inner = True)
    mech[keys[4]] = l_t_i
    l_t = Mech(interface, names[5], keys[5], [x0-48,y0-160], data["Armor"]["T"], None, [-1,0, 1.5,0, 1.5,1, 0.5,1, 0.5,2, -1,2], l_t_i, [25, 35], [0,6,1,9], off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[5]] = l_t
    r_t_i = Mech(interface, names[6], keys[6], [x0+75,y0-160], data["Internal"]["T"], components[keys[6]], [-1,0, 1.5,0, 1.5,2, 0,2, 0,1, -1,1], c_t, [25, 35], [6,4,3,5], inner = True)
    mech[keys[6]] = r_t_i
    r_t = Mech(interface, names[7], keys[7], [x0+75,y0-160], data["Armor"]["T"], None, [-1,0, 1.5,0, 1.5,2, 0,2, 0,1, -1,1], r_t_i, [25, 35], [6,4,3,5], off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[7]] = r_t

    l_a_i = Mech(interface, names[8], keys[8], [x0-103,y0-160], data["Internal"]["A"], components[keys[8]], [0,0, 1,0, 1,2, 0,3, 0,4, 0.5,4, 0.5,5, -1,5, -1,1], l_t, [25, 25], [0,0,3,7], inner = True)
    mech[keys[8]] = l_a_i
    l_a = Mech(interface, names[9], keys[9], [x0-103,y0-160], data["Armor"]["A"], None, [0,0, 1,0, 1,2, 0,3, 0,4, 0.5,4, 0.5,5, -1,5, -1,1], l_a_i, [25, 25], [0,0,3,7], off_x = -1, off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[9]] = l_a
    r_a_i = Mech(interface, names[10], keys[10], [x0+143,y0-160], data["Internal"]["A"], components[keys[10]], [0,0, -1,0, -1,2, 0,3, 0,4, -0.5,4, -0.5,5, 1,5, 1,1], r_t, [25, 25], [0,0,3,7], inner = True)
    mech[keys[10]] = r_a_i
    r_a = Mech(interface, names[11], keys[11], [x0+143,y0-160], data["Armor"]["A"], None, [0,0, -1,0, -1,2, 0,3, 0,4, -0.5,4, -0.5,5, 1,5, 1,1], r_a_i, [25, 25], [0,0,3,7], off_x = 1, off_y = -1.7, fill_color="", outline_color="green")
    mech[keys[11]] = r_a

    l_l_i = Mech(interface, names[12], keys[12], [x0-10,y0-55], data["Internal"]["L"], components[keys[12]], [0,0, 0,7, 1,8, 1,9, -4,9, -4,8, -3,7, -3,1, -2,0], l_t, [15, 15], [2,14,3,15], inner = True)
    mech[keys[12]] = l_l_i
    l_l = Mech(interface, names[13], keys[13], [x0-10,y0-55], data["Armor"]["L"], None, [0,0, 0,7, 1,8, 1,9, -4,9, -4,8, -3,7, -3,1, -2,0], l_l_i, [15, 15], [2,14,3,15], off_x = -2.3, fill_color="", outline_color="green")
    mech[keys[13]] = l_l
    r_l_i = Mech(interface, names[14], keys[14], [x0+50,y0-55], data["Internal"]["L"], components[keys[14]], [0,0, 0,7, -1,8, -1,9, 4,9, 4,8, 3,7, 3,1, 2,0], r_t, [15, 15], [2,14,3,15], inner = True)
    mech[keys[14]] = r_l_i
    r_l = Mech(interface, names[15], keys[15], [x0+50,y0-55], data["Armor"]["L"], None, [0,0, 0,7, -1,8, -1,9, 4,9, 4,8, 3,7, 3,1, 2,0], r_l_i, [15, 15], [2,14,3,15], off_x = 2.3, fill_color="", outline_color="green")
    mech[keys[15]] = r_l

    r_c_t = Mech(interface, names[16], keys[16], [x0-5,y0+90], data["Armor"]["RC"], None, [0,0, 2,0, 2,2, 3,2, 3,5, 2,5, 2,7, 0,7, 0,5, -1,5, -1,2, 0,2], c_t_i, [25, 20], [0,2,1,13], off_y = 4.8, fill_color="light grey", outline_color="green")
    mech[keys[16]] = r_c_t
    r_l_t = Mech(interface, names[17], keys[17], [x0-48,y0+90], data["Armor"]["RT"], None, [-1,0, 1.5,0, 1.5,1, 0.5,1, 0.5,2, -1,2], l_t_i, [25, 35], [0,6,1,9], off_y = 1.7, fill_color="light grey", outline_color="green")
    mech[keys[17]] = r_l_t
    r_r_t = Mech(interface, names[18], keys[18], [x0+75,y0+90], data["Armor"]["RT"], None, [-1,0, 1.5,0, 1.5,2, 0,2, 0,1, -1,1], r_t_i, [25, 35], [6,4,3,5], off_y = 1.7, fill_color="light grey", outline_color="green")
    mech[keys[18]] = r_r_t

    #adding parents necessary for the work of some logic
    l_t_i._parents["LT"] = l_t
    l_t._parents["LAI"] = l_a_i
    l_a_i._parents["LA"] = l_a

    r_t_i._parents["RT"] = r_t
    r_t._parents["RAI"] = r_a_i
    r_a_i._parents["RA"] = r_a

    l_l_i._parents["LL"] = l_l
    r_l_i._parents["RL"] = r_l

    for key in keys:
        mech[key].draw()

    return mech


class Mech():
    def __init__(self, interface, name, key, coordinates, stat, components, polygon, child, scale, text_center, off_x = 0, off_y = 0, inner = False, fill_color = "pale green", outline_color = "red"):
        self._i = interface
        self._name = name
        self._key = key
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._stat = int(stat)
        self._components = components
        self._polygon = polygon
        self._damage = 0
        self._destroyed = False
        self._inner = inner
        self._fill = fill_color
        self._outline = outline_color
        self._child = child
        self._parents = {}
        self._scale_x = scale[0]
        self._scale_y = scale[1]
        self._text_center = text_center
        self._off_x = off_x
        self._off_y = off_y

    def draw(self):
        used_coordinates = []
        for i in range(len(self._polygon)):
            if i%2 == 0:
                used_coordinates.append(self._polygon[i]*self._scale_x + self._x)
            else:
                used_coordinates.append(self._polygon[i]*self._scale_y + self._y)
        center_x = (used_coordinates[self._text_center[0]] + used_coordinates[self._text_center[1]])/2 + self._off_x*self._scale_x
        center_y = (used_coordinates[self._text_center[2]] + used_coordinates[self._text_center[3]])/2 + self._off_y*self._scale_y
        self._polygon = self._i._canvas.create_polygon(used_coordinates, fill=self._fill, outline=self._outline, width = 3)
        if self._inner == False:
            self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",9, "bold"))
        else:
            self._text = self._i._canvas.create_text(center_x,center_y, anchor="center", justify="center", text=f"{self._damage}\n/\n{self._stat}", font=("arial",7, "normal"))

    def damage(self, damage, through = False):
        self._damage += damage
        damage_spill = 0
        if self._damage < self._stat:
            if damage > 0:
                print(f"*** Do {damage} to {self._name}")

            if self._damage >= self._stat/2 and self._inner == False:
                self._i._canvas.itemconfig(self._polygon, outline="dark orange", width = 3)
            elif self._damage >= self._stat/2 and self._inner == True:
                self._i._canvas.itemconfig(self._polygon, fill="orange", width = 3)

            if (self._inner == True) or (through == True):
                i = get_random_crit()
                #print(i)
                if i == 3 and (self._key == "HI" or self._key == "LAI" or self._key == "RAI" or self._key == "LLI" or self._key == "RLI"):
                    self.destroy()
                else:
                    if self._inner == True:
                        self._components.damage(i)
                    else:
                        self._child._components.damage(i)

        else:
            damage_spill = self._damage - self._stat
            self._damage -= damage_spill
            damage_done = damage - damage_spill

            if damage_done > 0:
                print(f"*** Do {damage_done} to {self._name}")
            if self._destroyed == False:
                print(f"{self._name} is destroyed!")
                self._destroyed = True

            if self._key == "LTI" and self._parents["LT"]._parents["LAI"]._destroyed == False:
                self._parents["LT"]._parents["LAI"].destroy()
            elif self._key == "RTI" and self._parents["RT"]._parents["RAI"]._destroyed == False:
                self._parents["RT"]._parents["RAI"].destroy()

            if self._inner == False:
                self._i._canvas.itemconfig(self._polygon, outline="red", width = 3)
                self._i._canvas.tag_lower(self._polygon)
                #self._i._canvas.delete(self._polygon)
            else:
                self._i._canvas.itemconfig(self._polygon, fill="red", outline="black", width = 3)
                self._components.destroy()
            
            if self._child == None:
                print("!!! Mech is destroyed !!!")
            elif self._child != None:
                self._i._canvas.itemconfig(self._text, font=("arial",7, "normal"))
                self._child._i._canvas.itemconfig(self._child._text, font=("arial",9, "bold"))
                self._child.damage(damage_spill)
        
        self._i._canvas.itemconfig(self._text, text=f"{self._damage}\n/\n{self._stat}")
        
    def destroy(self):
        self._destroyed = True
        self._damage = self._stat
        self._i._canvas.itemconfig(self._text, text=f"{self._damage}\n/\n{self._stat}", font=("arial",7, "normal"))

        if self._inner == False:
            self._i._canvas.itemconfig(self._polygon, outline="red", width = 3)
            self._i._canvas.tag_lower(self._polygon)
        else:
            self._i._canvas.itemconfig(self._polygon, fill="red", outline="black", width = 3)
            self._components.destroy()

        if self._parents != {}:
            print(f"{self._name} is blown off!")
            for key in self._parents.keys():
                self._parents[key].destroy()