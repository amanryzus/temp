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
