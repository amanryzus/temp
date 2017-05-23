from sys import argv
w=[int(x) for x in argv[1:]]
print (w)


class Valu(Exception):
    pass


try:
    n1=w[0]
    n2=w[1]
    n3=w[2]

    if (n1<0):
        raise Valu
    if (n1<20 or n2 <20 or n3 <20):
        raise TypeError

except TypeError :
    print("Wront Type !!")
except Valu:
    print('ijoimnokm')
