#question 8 part-A
'''import tkinter as tk
from itertools import count
def start_counter(label):
    counter = count(0)
    def update_func():
        label.config(text=str(counter.__next__()))
        label.after(1000, update_func)
    update_func()

root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="red")
label.pack()
start_counter(label)
button = tk.Button(root, text='Stop', width=30, command=root.destroy)
button.pack()
root.mainloop()'''



#question 8 part-B
import re
n=int(input(" enter the no. of persons "))
print("now enter the names, phone number and email id's of ",n," persons")
b=[]
cont=0
for i in range(n):
    a=[z for z in input().split()]
    result=re.match("^\d{2,3}-\d{8}$",a[1])
    if result!=None:
        print(("COrrest Phone format !!"))
        pat="0000$"
        result1=re.match(pat,a[1])
        if (result1):
            print("The no as 0000 at last!")
    else:
        b.append(a[0])
    pattern = "([\w]+)@([a-z]+).(com|org|edu)"
    email = re.match(pattern,a[2])
    host = email.group(2)
    if host == "gmail":
        cont+=1
print(b,cont,)

'''






from tkinter import*
from tkinter.messagebox import*
root = Tk()
v = IntVar()

Label(root,text="Value 1").pack()
E1=Entry(root)
E1.pack()
Label(root,text="Value 2").pack()
E2=Entry(root)
E2.pack()

operations = [("Add",1),("Subtract",2),("Multiply",3),("Divide",4)]

def do():
    x=int(E1.get().strip())
    y=int(E2.get().strip())

    result.delete(0,10)
    if v.get()==1:
        ans=x+y
    if v.get()==2:
        ans=x-y
    if v.get()==3:
        ans=x*y
    if v.get()==4:
        ans=x/y
    result.insert(0,ans)


for txt, val in operations:
    Radiobutton(root,text=txt,variable=v,command=do,value=val).pack()

Label(root,text="Choose what you want to do:").pack()
Label(root,text="Result").pack()
result=Entry(root)
result.pack()
mainloop()
'''


















