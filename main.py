from window import Window, Point
from interface import Interface
from mech import Mech


def main():
    win = Window(1280, 720)
    interface = Interface(win)
    
    mech = Mech(interface, Point(250,250))
    interface._mech = mech

    win._root.mainloop()

main()