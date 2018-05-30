from tkinter import *
from tkinter import filedialog


def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


def FontHelvetica():
    global text
    text.config(font="Helvetica")


def FontCourier():
    global text
    text.config(font="Courier")


root = Tk()
root.title('Text Editor')
text = Text(root)
text.grid()
button = Button(root, text="Save", command=saveAs)
button.grid()
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font['menu'] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
root.mainloop()
