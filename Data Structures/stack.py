stack=[]
def push():
    element=input("enter the element to be inserted:")
    stack.append(element)
    print(stack)    
    return

def pop():
    if len(stack)==0:
        print("the stack is empty")
    else:
        e=stack.pop()
        print("the removed element is:",e)
        print(stack)

def full():
    print("the stack is overloaded")
    print("select one option to perform operation on stack:")
    print("enter \"2\" for removing an element")
    print("enetr \"3\" to exit")
    choice=int(input("please enter your choice:"))
    if choice==2:
        pop()
    elif choice==3:
        exit
    else:
        print("please enter a valid choice")


def empty():
    print("the stack is empty")
    print("select one option to perform operation on stack:")
    print("enter \"1\" for inserting an element")
    print("enetr \"3\" to exit")
    choice=int(input("please enter your choice:"))
    if choice==1:
        push()
    elif choice==3:
        exit
    else:
        print("please enter a valid choice")
n=int(input("please enter the limit of stack:"))
while True:
    print("select one option to perform operation on stack:")
    print("enter \"1\" for pushing an element")
    print("enter \"2\" for removing an element")
    print("enetr \"3\" to exit")
    choice=int(input("please enter your choice:"))
    if choice==1:
        if len(stack)>n-1:
            full()
        else:
            push()
    elif choice==2:
        if len(stack)==0:
            empty()
        else:
            pop()
    elif choice==3:
        break
    
    else:
        print("please enter a valid choice")
