from tkinter import *

# Window Settings
window = Tk()
window.title("Lists")

# Size (width, height)
window.geometry("400x300")
window.maxsize(500, 500)
window.minsize(200, 200)
window.resizable(True, True)

# Widgets

# Whole Frame
inputFrame = LabelFrame(text='Write down an important task', width=200, height=150)
# Top Frame
topFrame = Frame(inputFrame, width=200, height=150)
# Two frames (L/R)
# L
leftFrame = Label(topFrame, padx=10, pady=10)
label1 = Label(leftFrame, text='Task')
taskEntry = Entry(leftFrame)
# R
rightFrame = Label(topFrame, padx=10, pady=10)
label2 = Label(rightFrame, text='Until when')
whenEntry = Entry(rightFrame, width=10)
# Da button
button1 = Button(inputFrame,bg='black')

# Bottom
bottomFrame = Frame(inputFrame, width=200, height=150)

inputFrame.pack()
# Top
topFrame.pack()
leftFrame.pack(side=LEFT)
label1.pack()
taskEntry.pack()
button1.pack()
rightFrame.pack(side=LEFT)
label2.pack()
whenEntry.pack()
# Bottom
bottomFrame.pack()
window.mainloop()
