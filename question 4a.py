def initials(name):
    s=name.split()
    s1=str("")
    #for i in range(len(s)):
    for x in s:
        s1=s1+x[0]
    return s1

name=input("enter the name")
string=initials(name)
print(string)
