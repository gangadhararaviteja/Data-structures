class node():
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head==None:
            print("empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"----->",end=" ")
                n=n.ref
    def add_empty(self,data):
        new_node=node(data)
        if self.head==None:
            new_node=self.head
        else:
            print(" ")
            print("linked list is not empty to add the element")
            print(" ")
    def add_beg(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        new_node=node(data)
        n=self.head
        while n!=None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n==None:
            print(" ")
            print("the node is not found")
            print(" ")
        else:
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head==None:
            print(" ")
            print("linked list is empty")
            print(" ")
        elif self.head.data==x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n=self.head
            while n.ref!=None:
                if n.ref.data==x:
                    break
                else:
                    n=n.ref
            if n.ref==None:
                print(" ")
                print("the node is not found")
                print(" ")
            else:
                new_node = node(data)
                new_node.ref=n.ref
                n.ref=new_node

    def del_beg(self):
        if self.head==None:
            print(" ")
            print("the linked list is empty")
            print(" ")
        elif self.head.ref==None:
            self.head=None
            print(" ")
            print("the list has become empty")
            print(" ")
        else:
            self.head=self.head.ref

    def del_end(self):
        if self.head==None:
            print(" ")
            print("linked list is empty")
            print(" ")
        else:
            n=self.head
            while n.ref.ref!=None:
                n=n.ref
            n.ref=None


    def del_value(self,x):
        if self.head == None:
            print(" ")
            print("the linked list is empty")
            print(" ")
        elif self.head.data==x:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref!=None:
                if n.ref.data==x:
                    break
                else:
                    n=n.ref
            if n==None:
                print(" ")
                print("the node is not found")
                print(" ")
            else:
                n.ref=n.ref.ref

l=linkedlist()
while True:
    print(" ")
    print("enter \"1\" to add element into singly linked list")
    print("enter \"2\" to remove an element from singly linked list")
    print("enter \"3\" to traverse the linked list")
    print("enter \"4\" to exit")
    print(" ")
    choice = int(input("please enter your choice:"))
    if choice==1:
        print(" ")
        print("enter \"1\" to add at beggining of the list")
        print("enter \"2\" to add at end of the list")
        print("enter \"3\" to add after a specific node")
        print("enter \"4\" to ad before a specific element")
        print("enter \"5\" to exit")
        print(" ")
        c = int(input("enter your choice:"))
        if c==1:
            element=int(input("enter the element to be added:"))
            l.add_beg(element)
            print(" ")
            print("The linked list is:", end=" ")
            l.traversal()
            print(" ")
        elif c==2:
            element = int(input("enter the element to be added:"))
            l.add_end(element)
            print(" ")
            print("The linked list is:", end=" ")
            l.traversal()
            print(" ")
        elif c==3:
            element = int(input("enter the element to be added:"))
            p=int(input("enter a specific element after which you want to add the new element:"))
            l.add_after(element,p)
            print(" ")
            print("The linked list is:", end=" ")
            l.traversal()
            print(" ")
        elif c==4:
            element = int(input("enter the element to be added:"))
            p=int(input("enter a specific element before which you want to add th new element:"))
            l.add_before(element,p)
            print(" ")
            print("The linked list is:", end=" ")
            l.traversal()
            print(" ")
        elif c==5:
            break
        else:
            print("enetr the correct choice")
    elif choice==2:
        print("enter \"1\" to delete at begining of the list")
        print("enter \"2\" to delete at end of the list")
        print("enter \"3\" to delete a specific node")
        print("enter \"4\" to exit")
        c = int(input("enter your choice:"))
        if c==1:
            l.del_beg()
            print(" ")
            print("The linked list is:",end= " ")
            l.traversal()
            print(" ")
        elif c==2:
            l.del_end()
            print(" ")
            print("The linked list is:", end=" ")
            l.traversal()
            print(" ")
        elif c==3:
            element = int(input("enter the element to be deleted:"))
            l.del_value(element)
            print(" ")
            print("The linked list is:", end=" ")
            l.traversal()
            print(" ")
        elif c==4:
            break
        else:
            print(" ")
            print("eneter the correct choice")
    elif choice==3:
        print(" ")
        print("The linked list is:", end=" ")
        l.traversal()
        print(" ")
    elif choice==4:
        break
    else:
        print(" ")
        print("please enter a correct choice")
