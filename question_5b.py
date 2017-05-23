#question 5 part-A
'''def vowelcount(string):
    dict={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in string:
        if i=='a':
            dict[i]+=1
        elif i=='e':
            dict[i]+=1
        elif i=='i':
            dict[i]+=1
        elif i=='o':
            dict[i]+=1
        elif i=='u':
            dict[i]+=1
    print(sorted(dict.items()))

string=input("enter the string")
vowelcount(string)'''


#question 5 part-B

class triangle:
    no_of_sides=3
    sum=0
    def __init__(self,a1,a2,a3):
        self.angle1=a1
        self.angle2=a2
        self.angle3=a3
        triangle.sum=a1+a2+a3
    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3)==180:
            return "true"
        else:
            return "false"
a1,a2,a3=map(int,input("enter the three angles").split())
x=triangle(a1,a2,a3)
print(x.check_angles())
print(triangle.no_of_sides)
print(triangle.sum)






























