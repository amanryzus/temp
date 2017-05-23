#question 4 part-a

'''def initials(name):
    s=name.split()
    s1=str("")
    for i in range(len(s)):
        s1=s1+s[i][0]
    return s1

name=input("enter the name")
string=initials(name)
print(string)'''

#question 4 part-b

class Adder:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        try:
            raise NotImplementedError
        except NotImplementedError:
            print('not implemented')
class ListAdder(Adder):
    def __init__(self,x):
        Adder.__init__(self,x)
        self.list=x
    def __add__(self, other):
        return ListAdder(self.list+other.list)
class DictAdder(Adder):
    def __init__(self,x):
        Adder.__init__(self,x)
        self.Dict=x
    def __add__(self, other):
        z = self.Dict.copy()
        z.update(other.Dict)
        return DictAdder(z)
x=Adder([1,2,3,4])
y=Adder([2,3,3,6,4,5])
q=ListAdder([1,2,3,4])
w=ListAdder([2,3,3,6,4,5])
a=DictAdder({1:1,2:2,3:3})
s=DictAdder({4:4,5:5,6:6})
z=x+y
if z!=None:
    print(z.list)
e=w+q
if e!=None:
    print(e.list)
d=a+s
if d!=None:
    print(d.Dict)







