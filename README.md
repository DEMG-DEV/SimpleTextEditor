# SimpleTextEditor
In this Repository I will be teaching you how to create a simple text editor with Python and the module Tkinter in Python 3.

To do this tutorial you need some basic knowledge of Python 3.

First create a python file called [main.py](main.py) or something like that. Then open it with a text editor like Atom, Notepad ++ or VS Code.

## Step 1: Making a Window
To make a text editor we need a window. Type in the file:
```
from tkinter import *


root=Tk()
root.title("Text Editor")
root.mainloop()
```
Then if you are on a mac go Cmd+Shift - search and open "terminal" - then type
```
python /pathto/texteditor.py 
and hit enter.
```

If you are on a windows, search and open Command prompt, type
```
python /pathto/texteditor.py
and hit enter. You should se a screen that looks like the picture above.
```

Congrats!

## Step 2: Add a Text Widget
Now we need to add something to type in.

Underneath root=Tk() add two lines like this:

```
text=Text(root)
text.grid()
```
Then run the file again like in step one. You should get a bigger screen with a text box in it when you click on it. It will look like the picture above.

Your full code will look like this now:
```
from tkinter import *


root=Tk()
root.title("Text Editor")
text=Text(root)
text.grid()
root.mainloop()
```

## Step 3: Saving Your Text
You need to be able to save your text of course, so we will add a button to save.

Under import Tkinter add

```
from tkinter import filedialog
```

Under the last line you added write this:

```
def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
```

and under add the Text component write this:
```
button = Button(root, text="Save", command=saveAs)
button.grid()
```

Clicking on the button will save your file.

The full code:

```
from tkinter import *


def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
    
root=Tk()
root.title("Text Editor")
text=Text(root)
text.grid()
button = Button(root, text="Save", command=saveAs)
button.grid()
root.mainloop()
```

## Step 4: Font Changer
Under the last line you added, add this:

```
def FontHelvetica():
   global text
    text.config(font="Helvetica")
    
def FontCourier():
    global text
    text.config(font="Courier")
```

under add the button component write this code:
```
font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
helvetica=IntVar() 
courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
```
Congratulations! You have finished a very simple text editor.

Run the file to use it!

Full Code:
```
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
```
