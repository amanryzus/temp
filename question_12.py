#question 12 part-A

from mystring import palin
from mystring import camel
from mystring import vowel
string=input("enter the string ")
while 1:
    ch=int(input("1:palindrome  2:countvowel  3:camelcase 4:exit "))
    if ch==1:
        palin.palin(string)
    elif ch==2:
        vowel.vowel(string)
    elif ch==3:
        camel.cam(string)
    elif ch==4:
        exit()


#question 12 part-B

'''try:
    print(1+'msrit')
except TypeError:
    print("type error")

try:
    l=[1,2,3]
    print(l[4])
except IndexError:
    print("index error")'''

