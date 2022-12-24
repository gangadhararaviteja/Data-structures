queue=[]
def enqueue():
    element=input("enter the element to be inserted:")
    queue.append(element)
    print(queue)    


def dequeue():
    if len(queue)==0:
        print("the queue is empty")
    else:
        e=queue.pop(0)
        print("the removed element is:",e)
        print(queue)

def isfull():
    print("the queue is full")
    print("select one option to perform operation on queue:")
    print("enter \"2\" for removing an element")
    print("enter\"3\" for dispalying the queue")
    print("enetr \"4\" to exit")
    print("enter \"5\" to check the element to be removed next")
    choice=int(input("please enter your choice:"))
    if choice==2:
        enqueue()
    elif choice==4:
        exit
    elif choice==3:
        display()
    elif choice==5:
        front()
    else:
        print("please enter a valid choice")


def isempty():
    print("the queue is empty")
    print("select one option to perform operation on queue:")
    print("enter \"1\" for inserting an element")
    print("enter\"3\" for dispalying the queue")
    print("eneter \"4\" to exit")
    print("enter \"5\" to check the element to be removed next")
    choice=int(input("please enter your choice:"))
    if choice==1:
        dequeue()
    elif choice==4:
        exit
    elif choice==3:
        display()
    elif choice==5:
        front()
    else:
        print("please enter a valid choice")
def display():
    print(queue)
def front():
    print(queue[0])
n=int(input("please enter the limit of queue:"))
while True:
    print("select one option to perform operation on queue:")
    print("enter \"1\" for inserting an element")
    print("enter \"2\" for removing an element")
    print("enter\"3\" for dispalying the queue")
    print("enetr \"4\" to exit")
    print("enter \"5\" to check the element to be removed next")
    choice=int(input("please enter your choice:"))
    if choice==1:
        if len(queue)>n-1:
            isfull()
        else:
            enqueue()
    elif choice==2:
        if len(queue)==0:
            isempty()
        else:
            dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    elif choice==5:
        front()
    
    else:
        print("please enter a valid choice")
