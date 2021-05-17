# import from tkinter
import tkinter
from tkinter import *

root = Tk() # create root window
root.title("BMI")
root.config(bg="skyblue")
root.geometry("500x500")


# Create Frame widget



#

# creating labels

label_text =StringVar

label_1 = Label(root, text="insert weight")
label_1.place(x=10, y=10 )
weight = Entry(root)
weight.place(x=250, y=10)

label_2 = Label(root, text="insert heihgt")
label_2.place(x=10,y=40 )
height = Entry(root)
height.place(x=250, y=40)

label_3 = Label(root, text="gender:").place(x=10, y=80)
tkinter.Radiobutton(root, text="Male", ).place(x=90, y=80)
tkinter.Radiobutton(root, text="Female",).place(x=90, y=100)

label_4 = Label(root, text="Age:").place(x=250,y=80 )
age=Entry(root).place(x=300,y=80)

label_5 = Label(root, text="Answer: ").place(x=10, y=150)
answer = Label(root, text="", textvariable=label_text ).place(x=80, y=150)

#defy functions

def calculate_BMI():
    w = float(weight.get())
    h = float(height.get())
    aswer = float(w/((h/100)**2))
    age.insert(0, aswer)


calculate_BMI = Button(root, text="Convert", command=calculate_BMI).place(x=350, y=120)

root.mainloop()