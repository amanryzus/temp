#a=[int(z) for z in input("enter the elements").split()]
a=list(map(int,input("Enter the elements").split()))
print(a)
x=a[0]
b=[]
for i in range(1,len(a)):
    b.append(a[i])
b.append(x)
a=b
print(a)
