import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.title("Calc")
tk.config()
tk.geometry("400x400")

l1=tkinter.Label(text="Enter First Value")
l1.place(x=0,y=0)
t1=tkinter.Entry()
t1.place(x=25,y=25)

l2=tkinter.Label(text="Enter Second Value")
l2.place(x=0,y=50)
t2=tkinter.Entry()
t2.place(x=25,y=75)

def plus():
    n1=t1.get()
    n2=t2.get()
    print("Sum Is:",int(n1)+int(n2))
def sub():
    n1=t1.get()
    n2=t2.get()
    print("Sub Is:",int(n1)-int(n2))
def multi():
    n1=t1.get()
    n2=t2.get()
    print("Multi Is:",int(n1)*int(n2))
def div():
    n1=t1.get()
    n2=t2.get()
    print("Division Is:",int(n1)/int(n2))


btn1=tkinter.Button(text="+",fg='blue',font='Consolas 25 bold',command=plus)
btn1.place(x=25,y=125)
btn2=tkinter.Button(text="-",fg='blue',font='Consolas 25 bold',command=sub)
btn2.place(x=125,y=125)
btn3=tkinter.Button(text="*",fg='blue',font='Consolas 25 bold',command=multi)
btn3.place(x=225,y=125)
btn4=tkinter.Button(text="/",fg='blue',font='Consolas 25 bold',command=div)
btn4.place(x=325,y=125)
tk.mainloop()





