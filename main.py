from window import Window, Interface


def main():
    win = Window(1280, 720)
    interface = Interface(win)

    win._root.mainloop()

main()