queue=[]
s=list()   
def enqueue():
    element=int(input("enter the element to be inserted:"))
    print(" ")
    queue.append(element)
    print(queue)
    print(" ")
    s.append(element)

def LTH():
    queue.sort()
    x=queue.pop(0)
    s.remove(x)
    print(" ")
    print("the element removed is:",x)
    print(" ")
    print(s)
    print(" ")


def HTL():
    queue.sort()
    x=queue.pop()
    s.remove(x)
    print(" ")
    print("the element removed is",x)
    print(" ")
    print(s)
    print(" ")


while True:
    print("enter \"1\" to insert an element")
    print("enter \"2\" to remove an element")
    print("enter \"3\" to exit")
    print(" ")
    choice=int(input("please enter your choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        if len(queue)==0:
            print(" ")
            print("the queue is empty")
            print(" ")
        else:
            print(" ")
            print("enter \"1\" to remove elemnet with highest priority")
            print("enter \"2\" to remove element with lowest priority")
            print("enter \"3\" to exit")
            print("[***NOTE:\"Here highest number is assigned with highest priority\"***]")
            print(" ")
            c=int(input("please enter your choice:"))
            if c==1:
                HTL()
            elif choice==2:
                LTH()
            elif choice==3:
                break
            else:
                print("please enter a valid choice") 

    elif choice==3:
        break
    else:
        print("please enter a valid choice") 

