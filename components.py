import random

from tkinter import *


def initialize_components(interface, data, x0, y0):
    components = {}
    names = ["Head", "Cetner Torso", "Left Torso", "Right Torso", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
    keys = ["HI", "CTI", "LTI", "RTI", "LAI", "RAI", "LLI", "RLI"]

    h = Table(interface, names[0], keys[0], [x0-60,y0], data["Head"], 6, [120,20])
    components[keys[0]] = h
    c_t = Table(interface, names[1], keys[1], [x0-60,y0+170], data["Center Torso"], 12, [120,20])
    components[keys[1]] = c_t
    l_t = Table(interface, names[2], keys[2], [x0-200,y0], data["Left Torso"], 12, [120,20], c_t)
    components[keys[2]] = l_t
    r_t = Table(interface, names[3], keys[3], [x0+80,y0], data["Right Torso"], 12, [120,20], c_t)
    components[keys[3]] = r_t
    l_a = Table(interface, names[4], keys[4], [x0-340,y0], data["Left Arm"], 12, [120,20], l_t)
    components[keys[4]] = l_a
    r_a = Table(interface, names[5], keys[5], [x0+220,y0], data["Right Arm"], 12, [120,20], r_t)
    components[keys[5]] = r_a
    l_l = Table(interface, names[6], keys[6], [x0-270,y0+290], data["Left Leg"], 6, [120,20], l_t)
    components[keys[6]] = l_l
    r_l = Table(interface, names[7], keys[7], [x0+150,y0+290], data["Right Leg"], 6, [120,20], r_t)
    components[keys[7]] = r_l

    for key in keys:
        components[key].draw()

    return components


class Table():
    def __init__(self, interface, name, key, coordinates, data, size, scale, child=None):
        self._i = interface
        self._data = data
        self._name = name
        self._key = key
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._polygon = [0,0, 1,0, 1,1, 0,1]
        self._size = size
        self._scale_x = scale[0]
        self._scale_y = scale[1]
        self._child = child
        self._part = None

        if self._size != 6 and self._size != 12:
            raise Exception("The size can only be 6 or 12")

    def draw(self):
        title = self._i._canvas_2.create_text(self._x+self._scale_x/2, self._y-self._scale_y, anchor="center", justify="center", text=self._name, font=("arial",9, "bold"))
        self.tables = []
        self.component_status = []
        for j in range(self._size):
            used_coordinates = []
            for i in range(len(self._polygon)):
                if i%2 == 0:
                    used_coordinates.append(self._polygon[i]*self._scale_x + self._x)
                else:
                    used_coordinates.append(self._polygon[i]*self._scale_y + self._y + j*self._scale_y) 
            center_x = (used_coordinates[0] + used_coordinates[2])/2
            center_y = (used_coordinates[1] + used_coordinates[5])/2
            polygon = self._i._canvas_2.create_polygon(used_coordinates, fill="", outline="black", width = 2)
            text_value = self._data[j+1]
            if text_value == "":
                self.component_status.append(False)
                text_value = "---"
            else:
                self.component_status.append(True)
            text = self._i._canvas_2.create_text(center_x,center_y, anchor="center", justify="center", text=text_value, font=("arial",8, "normal"))
            self.tables.append([polygon, text])

    def destroy(self):
        for i in range(len(self.tables)):
            self._i._canvas_2.itemconfig(self.tables[i][0], fill="red")
            if self.component_status[i] == True:
                self.component_status[i] = False
                self._i._canvas_2.itemconfig(self.tables[i][1], font=("arial", 8, "overstrike"))


    #at the moment, there is a check for the ammo explosion but no check if armor on the exploded side is destroed. It is a small thing, will solve when I have time..         
    def damage(self, crits):
        if True in self.component_status:
            for i in range(crits):
                not_hit = True
                while not_hit:
                    item = random.randint(1, self._size) - 1
                    if self.component_status[item] == True:
                        print(f"Critical hit! {self._data[item+1]} is destroyed!")
                        not_hit = False
                        self.component_status[item] = False
                        self._i._canvas_2.itemconfig(self.tables[item][0], fill="red")
                        self._i._canvas_2.itemconfig(self.tables[item][1], font=("arial", 8, "overstrike"))
                        if "Ammo" in self._data[item+1]:
                            self._part.damage(100)
                            return
                        if "Engine" in self._data[item+1]:
                            self._i._engine_hit += 1
                        if "Gyro" in self._data[item+1]:
                            self._i._gyro_hit += 1
                        if "Sensors" in self._data[item+1]:
                            self._i._sensor_hit += 1
                        if "Life" in self._data[item+1]:
                            self._i._life_support += 1
                        if "Sink"in self._data[item+1]:
                            self._i._mech_data["Heat Sink"] = str(int(self._i._mech_data["Heat Sink"])-1)
                            self._i._mech_label_3.configure(text=f"Heat Sinks: {self._i._mech_data["Heat Sink"]}")

                if True not in self.component_status:
                    break

        else:
            if self._child !=None:
                self._child.damage(crits)


