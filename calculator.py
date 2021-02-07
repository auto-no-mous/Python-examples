from tkinter import *
import math
root=Tk()
root.title("Calculator")
fr=Frame(root)
fr.grid()
en1=Entry(fr, text='0', width=20)

#пытаемся выполнить выражение
def equal():
    try: 
            value= eval(en1.get()) 
    except Exception:
            en1.delete(0,END)
            en1.insert(0,'Invalid Input!')
    else:
            en1.delete(0, END)
            en1.insert(0, value)
            
#обработчик нажатия на кнопку        
def action(arg): 
    en1.insert(END,arg)

def clear():
    en1.delete(0, END)

def sqrt():
    try: 
        value= eval(en1.get()) 
    except SyntaxError or NameError:
        en1.delete(0,END)
        en1.insert(0,'Invalid Input!')
    else:
        en1.delete(0, END)
        en1.insert(0, math.sqrt(value))

#цифровые кнопки
en1.grid(row=0,column=0,columnspan=3)
b1=Button(fr, text='1', width=5, command=lambda: action("1"))
b1.grid(row=1,column=0)
b2=Button(fr, text='2', width=5, command=lambda: action("2"))
b2.grid(row=1,column=1)
b3=Button(fr, text='3', width=5, command=lambda: action("3"))
b3.grid(row=1,column=2)
b4=Button(fr, text='4', width=5, command=lambda: action("4"))
b4.grid(row=2,column=0)
b5=Button(fr, text='5', width=5, command=lambda: action("5"))
b5.grid(row=2,column=1)
b6=Button(fr, text='6', width=5, command=lambda: action("6"))
b6.grid(row=2,column=2)
b7=Button(fr, text='7', width=5, command=lambda: action("7"))
b7.grid(row=3,column=0)
b8=Button(fr, text='8', width=5, command=lambda: action("8"))
b8.grid(row=3,column=1)
b9=Button(fr, text='9', width=5, command=lambda: action("9"))
b9.grid(row=3,column=2)
b0=Button(fr, text='0', width=5, command=lambda: action("0"))
b0.grid(row=4,column=0)

#кнопки операций
b_plus=Button(fr, text='+', width=5, command=lambda: action("+"))
b_plus.grid(row=1,column=3)
b_minus=Button(fr, text='-', width=5, command=lambda: action("-"))
b_minus.grid(row=2,column=3)
b_div=Button(fr, text='/', width=5, command=lambda: action("/"))
b_div.grid(row=3,column=3)
b_multy=Button(fr, text='*', width=5, command=lambda: action("*"))
b_multy.grid(row=4,column=3)
b_sqrt=Button(fr, text='sqrt', width=5, command=sqrt)
b_sqrt.grid(row=4,column=1)
b_pow=Button(fr, text='^', width=5, command=lambda: action("**"))
b_pow.grid(row=4,column=2)
b_clear=Button(fr, text='C', width=5, command=clear)
b_clear.grid(row=0,column=3)
b_eq=Button(fr, text='=', width=25, command=lambda:equal())
b_eq.grid(row=5,column=0, columnspan=4)


root.mainloop()
