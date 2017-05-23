from tkinter import *
root = Tk()
root.title(" Basic Calculator ")
l1=Label(root, text="a").grid(row=0)
l2=Label(root, text="b").grid(row=1)
l3=Label(root,text="result").grid(row=2)

e1 = Entry(root,width=20)
e1.grid(row=0,column=1)
e2 = Entry(root,width=20)
e2.grid(row=1,column=1)
#e1.grid(row=0,column=1)
e3=Entry(root,width=20)
e3.grid(row=2,column=1)
myvar=IntVar()



def callback():
    total = int(e1.get()) + int(e2.get())
    e3.delete(0, END)
    e3.insert(0, str(total))
b =Radiobutton(root, text=" add ",variable=myvar,value=5,command=callback)
b.grid(row=3,column=0)


def callback1():
    total = int(e1.get())-int(e2.get())
    e3.delete(0, END)
    e3.insert(0, str(total))
b1 =Radiobutton(root, text=" sub ",variable=myvar,value=15,command=callback1)
b1.grid(row=4,column=0)


def callback2():
    total = int(e1.get()) * int(e2.get())
    e3.delete(0, END)
    e3.insert(0, str(total))
b2 =Radiobutton(root, text=" Mul ",variable=myvar,value=25,command=callback2)
b2.grid(row=5,column=0)


def callback3():
    total = int(e1.get()) // int(e2.get())
    e3.delete(0, END)
    e3.insert(0, str(total))
b3 =Radiobutton(root, text=" div ",variable=myvar,value=35,command=callback3)
b3.grid(row=6,column=0)

#for widget in (e1,e2,l, b, b1, b2, b3):
#    widget.pack()
root.mainloop()
