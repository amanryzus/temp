# question 1 part-a

'''other way of input in list
n=int(input("enter the size"))
a=[]
for i in range(n):
    z=int(input())
    a.append(z)
print(a)'''

'''a=[int(z) for z in input("enter the elements").split()]
print(a)
x=a[0]
b=[]
for i in range(1,len(a)):
    b.append(a[i])
b.append(x)
a=b
print(a)'''



#question 1 part-b

'''name=input("enter the file name")
with open(name,"w") as file:
    file.write("ankit is a good boy\n")
    file.write("he studies in msrit\n")
    file.write("he plays daily\n")

def line_count():
    with open(name,"r") as file:
        l1=file.readlines()
    print("no. of lines: ",len(l1))

def word_count():
    with open(name,"r")as file:
        l2=file.read()
        l3=l2.split()
    print("no. of words : ",len(l3))

def char_count():
    with open(name,"r")as file:
        l4=file.read()
    print("no. of characters ",len(l4))

line_count()
word_count()
char_count()'''


#question 2 part-a
'''date=[int(z) for z in input("Enter a date in DD/MM/YY format:").split('/')]
print(date)
dict={1:'jan',2:'feb',3:'march',4:'april',5:'may',6:'june',7:'july',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}

if(date[0]==1):
    print(str(date[0])+"st "+dict[date[1]]+ " " + str(date[2]))

elif (date[0]==2):
    print(str(date[0])+"nd "+dict[date[1]]+ " " + str(date[2]))

elif date[0]==3:
    print(str(date[0])+"rd "+dict[date[1]]+ " " + str(date[2]))

else:
    print(str(date[0])+"th "+dict[date[1]]+ " " + str(date[2]))'''



#question 2 part-b
'''def censor(name):
    with open(name,"r")as file:
        l2=file.read()
        l3=l2.split()
    words=[]
    for i in l3:
        if len(i)==4:
            words.append('xxxx'+i)
    with open("censored.txt","w")as file:
        for i in words:
            file.write(i+'\n')

name=input("enter the name of file")
censor(name)'''




















