from tkinter import *

# Window Settings
from tkinter import filedialog

window = Tk()
window.title("Lists")

# Size (width, height)
window.geometry("400x600")
window.maxsize(500, 500)
window.minsize(200, 200)
window.resizable(True, True)

# Data taker function
counter = 0


def add():
    global counter
    text = taskEntry.get()
    text2 = whenEntry.get()
    counter += 1
    todolist.insert(END, str(counter) + ". " + text + "\t" + text2 + "\n")
    taskEntry.delete(0, END)
    whenEntry.delete(0, END)


def clear():
    todolist.delete(0.0, END)
    global counter
    counter = 0


def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(title='Save file',
                                    filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
                                    )
    if file:
        file.write(text)


def load():
    file = filedialog.askopenfile(title='Select file',
                                  filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
                                  )
    text = file.read()
    todolist.insert(END,text)


# Widgets

# Whole Frame
inputFrame = LabelFrame(text='Write down an important task', width=200, height=150)
# Top Frame
topFrame = Frame(inputFrame, width=200, height=150)
# Two frames (L/R)
# L
leftFrame = Label(topFrame, padx=10, pady=10)
label1 = Label(leftFrame, text='Task')
taskEntry = Entry(leftFrame, width=10)
# R
rightFrame = Label(topFrame, padx=10, pady=10)
label2 = Label(rightFrame, text='Until when')
whenEntry = Entry(rightFrame, width=10)
# Bottom
bottomFrame = Frame(inputFrame, width=200, height=150)
button1 = Button(bottomFrame, text='Create an important task', bg='black', command=add)

# After input
todolist = Text(width=15)
button2 = Button(text='Delete all tasks', bg='black', command=clear)
button3 = Button(text='Save', bg='black', command=save, width=10)
button4 = Button(text='Load', bg='black', command=load, width=10)

inputFrame.pack()
# Top
topFrame.pack()
leftFrame.pack(side=LEFT)
label1.pack()
taskEntry.pack()
rightFrame.pack(side=LEFT)
label2.pack()
whenEntry.pack()
# Bottom
bottomFrame.pack()
button1.pack()
# After
todolist.pack()
button2.pack()
button3.pack()
button4.pack()

window.mainloop()
