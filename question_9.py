z=int(input('balance'))
a=int(input('deposit'))
b=int(input('withdraw'))
try:
    if z+a-b<0:
        raise ValueError('invalid!')
    print("Amount remaining :",z+a-b)
except ValueError:
    print("invalid")




