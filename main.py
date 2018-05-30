from tkinter import *
from tkinter import filedialog


def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


root = Tk()
root.title('Text Editor')
text = Text(root)
text.grid()
button = Button(root, text="Save", command=saveAs)
button.grid()
root.mainloop()
