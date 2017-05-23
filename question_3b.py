#question 3 part-a

'''def insert():
    name=input("enter the phone name: ")
    price=input("enter its price")
    dict[name]=price
def search():
    name=input("enter the phone name to retreive its price")
    print(dict.get(name))

def price():
    price=input("enter the price which is of many phones")
    for i in dict.keys():
        if dict[i]==price:
            list.append(i)
    print(list)

def remove():
    name=input("enter the phone name to delete")
    del dict[name]

def display():
    #print(sorted(dict.items()))
    from operator import itemgetter
    print(sorted(dict.items(), key=itemgetter(1)))

dict={}
while 1:
    list=[]
    ch=int(input("enter your choice: 1:insert 2:search phone and its price 3:phones with same price 4:remove 5:display 6:exit  "))
    if ch==1:
        insert()
    elif ch==2:
        search()
    elif ch==3:
        price()
    elif ch==4:
        remove()
    elif ch==5:
        display()
    elif ch==6:
        exit()'''

#question 3 part-b

class account:
    def __init__(self,b,i,a):
        self.balance=b
        self.interst_rate=i
        self.account_number=a
    def add(self,interest):
        #print(x.balance,self.balance)
        self.balance=self.balance+interest
        print("the balance is ",self.balance)

    def withdraw(self,money):
        if (self.balance)>=1000:
            self.balance=self.balance-money
            print("the balance is ",self.balance)
        else:
            print("now account is below certain limit so extra money will be charged")
            self.balance=self.balance-money-200
            print("the balance is ",self.balance)


b,i,a=map(int,input("enter the balance interest rate and account number ").split())
x=account(b,i,a)
while 1:
    ch=int(input("enter your choice : 1:interest to add  2:withdraw money  3:exit "))
    if ch==1:
        interest=int(input("enter the interest to be added "))
        x.add(interest)
    elif ch==2:
        money=int(input("enter the money to be withdrawn "))
        x.withdraw(money)
    elif ch==3:
        exit()



