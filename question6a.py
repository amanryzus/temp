wd=[]
def f():
    str =" "
    for i in range (len(wd1)):
        str=str+" "+wd1[i]
    print (str)
    exit()
while 1:
    ip=input("Enter the lines :").split()
    wd.extend(ip)
    wd1=wd[::-1]
    for x in wd1:
        if (x=='quit'):
            del wd1[0]
            f()

