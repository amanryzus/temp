#question 11 part-A

'''def func(*args):
    a=[]
    for i in args:
        a.append(i)
    n=len(a)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

#variable arguments are collected as tuple
print(func(12,500,200,100,200,987,652,202022,981))'''

#question 11 part-B

class student():
    cont=0
    a=[]
    def __init__(self,usn,name,subject):
        self.u=usn
        self.n=name
        self.s=subject
    def increament(self):
        student.cont+=1
    def Python(self,n,subject):
        if self.s =='python':
            student.a.append(self.n)
    def display(self):
        print("students registered for python are :  ", student .a)
        print("total students are ",student.cont)

n=int(input("enter the no. of students"))
for i in range(n):
    usn,name,subject=map(str,input("enter the usn,name,subject registered of a student").split())
    x=student(usn,name,subject)
    x.increament()
    x.Python(name,subject)
x.display()



























