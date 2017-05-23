#question 10 part-A
'''def is_abecedarian(a):
    cont=0
    for i in a:
        if sorted(i)==list(i):
            cont+=1
    return cont

a=[z for z in input("enter the words").split()]
print(is_abecedarian(a))'''

#question 10 part-B
class Queue():
    rear=-1
    front=-1
    def __init__(self,q):
        self.queue=q

    def enque(self,element):
        try:
            if len(self.queue)>=5:
                raise ValueError
            Queue.rear+=1
            self.queue.append(element)
        except ValueError:
            print("queue is full")

    def deque(self):
        try:
            if Queue.rear == Queue.front:
                raise ValueError
            Queue.front+=1
            return self.queue.pop(0)
        except ValueError:
            print(" queue is empty ")


    def display(self):
        return self.queue

q=[]
x=Queue(q)
while 1:
    ch=int(input("1:insert  2:delete  3:display  4:exit  "))
    if ch==1:
        x.enque(int(input("enter element")))
    elif ch==2:
        print(x.deque())
    elif ch==3:
        print(x.display())
    elif ch==4:
        exit()
