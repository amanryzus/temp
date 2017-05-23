from mystring import camel
from mystring import vowel
from mystring import palin
while(1):
    if(int(input("do u wanna exit? press 1"))):
        exit()
    str=input("Enter the word")
    camel.cam(str)
    vowel.vowel(str)
    palin.palin(str)
