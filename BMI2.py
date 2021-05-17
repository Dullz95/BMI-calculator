from tkinter import *
from tkinter import ttk

root = Tk()
root.config(bg="skyblue")

#define functions
def bmi():
    r = int(e1.get())/((int(e2.get())/100)**2)
    label_text.set(r)


def ideal_bmi():
    if choice == "Male":
        r2 = 0.5 * int(e1.get())/((int(e2.get())/100)**2 + 11.5)
        label_text1.set(r2)
    else:
        r3 = 0.5 * int(e1.get())/((int(e2.get())/100)**2 + 0.03 * int(e3.get()) + 11)
        label_text1.set(r3)


def combinefunc(self, *funcs):
    def combinedfunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combinedfunc


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

#create size of window
root.geometry("1000x1000")
#create title
root.title("BMI Calculator")

label_text = StringVar()
label_text1 = StringVar()

# create labels
Label(root, text="Weight:").grid(row=5, column=2, )
Label(root, text="Height:").grid(row=6, column=2, )
Label(root, text="kg").grid(row=5, column=4, )
Label(root, text="cm").grid(row=6, column=4, )
Label(root, text="Gender: ").grid(row=7, column=2, )
Label(root, text="Age: ").grid(row=7, column=4, )
Label(root, text="Ideal BMI:").grid(row=9, column=4, )
result1 = Label(root, text="", textvariable=label_text).grid(row=9, column=3)
result2 = Label(root, text="", textvariable=label_text1).grid(row=9, column=5)
#create entries
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
# place entries
e1.grid(row=5, column=3)
e2.grid(row=6, column=3)
e3.grid(row=7, column=5)

gender = ["Male", "Female"]
# create choice option
choice = ttk.Combobox(root, values=gender)

choice.grid(row=7, column=3)
# create buttons
b1 = Button(root, text="Calculate Your Ideal BMI", command=combinefunc(bmi, ideal_bmi))
b2 = Button(root, text="Clear", command=clear)
b3 = Button(root, text="Exit", command=root.destroy)
#place buttons
b1.grid(row=8, column=2)
b2.grid(row=10, column=2)
b3.grid(row=10, column=4)


mainloop()
