#name=input("enter the file name")
name='idunno'
with open(name,"w") as file:
    file.write("RPGs are better than FPS\n")
    file.write("Skyrim is the best RPG ever\n")
    file.write("COD is the best FPS game ever !\n")

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
    sp=0
    with open(name,"r")as file:
        l4=file.read()
        for wd in l4:
            if(wd==' '):
                sp=(sp)+1

    print("no. of characters without spaces",len(l4)-sp)
    print("no. of characters with spaces",len(l4))

line_count()
word_count()
char_count()
