phone={}
ph=[]
pr=[]
q=1
def add():
    ph,pr=input("Enter the phone name and it price").split()
    if pr not in phone:
        phone[pr] = []
        phone[pr].append(ph)
    else:
        phone[pr].append(ph)
def find():
    k=int(input("Enter the price"))
    print(phone[k])
def rem():
    k=int(input("Enter the price to remove"))
    phone[k]=[]
def display():
    for x in phone.keys():
        print("At {0} Price the available phone :{1}".format(x,phone[x]))

while (q):
    q=int(input("Enter \n1 to add\n2 to find\n3 to remove\n4 to print\n0 to exit\n"))
    if q==1:
        add()
    elif q==2:
        find()
    elif q==3:
        rem()
    elif q==4:
        display()
