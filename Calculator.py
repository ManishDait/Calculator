from tkinter import *
from tkinter import font
window = Tk()
window.title("Calculator")
window.resizable(False, False)

def onButtonClick(value):
    current = textfield.get()
    textfield.delete(0, END)
    textfield.insert(0, str(current) + str(value))


def Clear():
    textfield.delete(0,END)


def Del():
    data = textfield.get()
    data = data[:-1]
    textfield.delete(0, END)
    textfield.insert(0, str(data))


def Calc():
    data = textfield.get()
    try:
        value = eval(data)
    
    except ZeroDivisionError:
        value = "Can not divide by zero"

    except:
        value = "Not a valid input"
    textfield.delete(0, END)
    textfield.insert(0, str(value))

textfield = Entry(window, width=40, borderwidth=1, font=("Arial", 16))
textfield.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttn_c = Button(window, width= 9, text="C", font=("Arial", 12), foreground="red", command=lambda: Clear())
buttn_c.grid(row=1, column=0)
buttn_del = Button(window, width= 9, text="Del", font=("Arial", 12), foreground="green", command=lambda: Del())
buttn_del.grid(row=1, column=1)
buttn_mod = Button(window, width= 9, text="%", font=("Arial", 12), foreground="green", command=lambda: onButtonClick("%"))
buttn_mod.grid(row=1, column=2)
buttn_div = Button(window, width= 9, text="/", font=("Arial", 12), foreground="green", command=lambda: onButtonClick("/"))
buttn_div.grid(row=1, column=3)

buttn_7 = Button(window, width= 9, text="7", font=("Arial", 12), command=lambda: onButtonClick(7))
buttn_7.grid(row=2, column=0)
buttn_8 = Button(window, width= 9, text="8", font=("Arial", 12), command=lambda: onButtonClick(8))
buttn_8.grid(row=2, column=1)
buttn_9 = Button(window, width= 9, text="9", font=("Arial", 12), command=lambda: onButtonClick(9))
buttn_9.grid(row=2, column=2)
buttn_mul = Button(window, width= 9, text="*", font=("Arial", 12), foreground="green", command=lambda: onButtonClick("*"))
buttn_mul.grid(row=2, column=3)

buttn_4 = Button(window, width= 9, text="4", font=("Arial", 12), command=lambda: onButtonClick(4))
buttn_4.grid(row=3, column=0)
buttn_5 = Button(window, width= 9, text="5", font=("Arial", 12), command=lambda: onButtonClick(5))
buttn_5.grid(row=3, column=1)
buttn_6 = Button(window, width= 9, text="6", font=("Arial", 12), command=lambda: onButtonClick(6))
buttn_6.grid(row=3, column=2)
buttn_sub = Button(window, width= 9, text="-", font=("Arial", 12), foreground="green", command=lambda: onButtonClick("-"))
buttn_sub.grid(row=3, column=3)

buttn_1 = Button(window, width= 9, text="1", font=("Arial", 12), command=lambda: onButtonClick(1))
buttn_1.grid(row=4, column=0)
buttn_2 = Button(window, width= 9, text="2", font=("Arial", 12), command=lambda: onButtonClick(2))
buttn_2.grid(row=4, column=1)
buttn_3 = Button(window, width= 9, text="3", font=("Arial", 12), command=lambda: onButtonClick(3))
buttn_3.grid(row=4, column=2)
buttn_add = Button(window, width= 9, text="+", font=("Arial", 12), foreground="green", command=lambda: onButtonClick("+"))
buttn_add.grid(row=4, column=3)

buttn_neg = Button(window, width= 9, text="+/-", font=("Arial", 12), command=lambda: onButtonClick("-"))
buttn_neg.grid(row=5, column=0)
buttn_0 = Button(window, width= 9, text="0", font=("Arial", 12), command=lambda: onButtonClick(0))
buttn_0.grid(row=5, column=1)
buttn_00 = Button(window, width= 9, text="00", font=("Arial", 12), command=lambda: onButtonClick("00"))
buttn_00.grid(row=5, column=2)
buttn_point = Button(window, width= 9, text=".", font=("Arial", 12), command=lambda: onButtonClick("."))
buttn_point.grid(row=5, column=3)

buttn_bo = Button(window, width= 9, text="(", font=("Arial", 12), command=lambda: onButtonClick("("))
buttn_bo.grid(row=6, column=0)
buttn_bc = Button(window, width= 9, text=")", font=("Arial", 12), command=lambda: onButtonClick(")"))
buttn_bc.grid(row=6, column=1)
buttn_point = Button(window, width= 23, text="=", font=("Arial", 12), background="green", foreground="white", command=lambda: Calc())
buttn_point.grid(row=6, column=2,columnspan=2)



window.mainloop()