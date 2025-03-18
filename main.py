from window import Window, Point
from interface import Interface
from mech import Center_Torso, Inner_Center_Torso


def main():
    win = Window(1280, 720)
    interface = Interface(win)
    
    i_c_t = Inner_Center_Torso(interface, Point(100,350), 10)
    c_t = Center_Torso(interface, Point(100,100), 20, i_c_t)
    
    interface._mech = c_t

    win._root.mainloop()

main()