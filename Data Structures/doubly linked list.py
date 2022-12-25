class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None
    def forward_traversal(self):
        if self.head==None:
            print("the linked list is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"---->",end=" ")
                n=n.next
    def backward_traversal(self):
        if self.head==None:
            print("the linkedlist is empty")
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            while n!=None:
                print(n.data,"---->",end=" ")
                n=n.prev


    def add_beg(self,data):
        new_node = node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=node(data)
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            n.next=new_node
            new_node.prev=n
    def add_after(self,data,x):
        new_node=node(data)
        if self.head==None:
            print("the list is empty")
        else:
            n=self.head
            while n!=None:
                if n.data==x:
                    break
                else:
                    n=n.next
            if n==None:
                ("the node is not found")
            else:
                n.next.prev=new_node
                new_node.next=n.next
                n.next=new_node
                new_node.prev=n
    def add_before(self,data,x):
        new_node=node(data)
        if self.head==None:
            print("the list is empty")
        else:
            if self.head.data==x:
                self.head.prev=new_node
                new_node.next=self.head
                self.head=new_node
            else:
                n=self.head
                while n.next!=x:
                    if n.data==x:
                        break
                    else:
                        n=n.next
                if n.next==None:
                    print("the node is not found")
                else:
                    new_node.next=n
                    new_node.prev=n.prev
                    n.prev.next=new_node
                    n.prev=new_node
    def del_beg(self):
        if self.head==None:
            print("the linked list is empty")
        elif self.head.next==None:
            self.head=None
            print("the linked list became empty")
        else:
            n=self.head
            self.head=n.next
            n.next.prev=None
    def del_end(self):
        if self.head==None:
            print("the linked is empty")
        elif self.head.next==None:
            self.head=None
            print("the linked list has become empty")
        else:
            n=self.head
            while n!=None:
                if n.next==None:
                    break
                else:
                    n=n.next
            n.prev.next=None
    def del_value(self,x):
        if self.head==None:
            print("the list is empty")
        elif self.head==x:
            n=self.head
            self.head=n.next
            n.next.prev=None
        else:
            n=self.head
            while n!=None:
                if n.data==x:
                    break
                else:
                    n=n.next
            if n==None:
                print("the element is not found")
            else:
                n.prev.next=n.next
                n.next.prev=n.prev


while True:
    print(" ")
    print("enter \"1\" to add element into doubly linked list")
    print("enter \"2\" to remove an element from doubly linked list")
    print("enter \"3\" to traverse the doubly linked list")
    print("enter \"4\" to exit")
    print(" ")
    choice = int(input("please enter your choice:"))
    if choice==1:
        print(" ")
        print("enter \"1\" to add at beggining of the list")
        print("enter \"2\" to add at end of the list")
        print("enter \"3\" to add after a specific node")
        print("enter \"4\" to add before a specific element")
        print("enter \"5\" to exit")
        print(" ")
        c = int(input("enter your choice:"))
        if c==1:
            element=int(input("enter the element to be added:"))
            l.add_beg(element)
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==2:
            element = int(input("enter the element to be added:"))
            l.add_end(element)
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==3:
            element = int(input("enter the element to be added:"))
            p=int(input("enter a specific element after which you want to add the new element:"))
            l.add_after(element,p)
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==4:
            element = int(input("enter the element to be added:"))
            p=int(input("enter a specific element before which you want to add th new element:"))
            l.add_before(element,p)
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==5:
            break
        else:
            print("enter the correct choice")
    elif choice==2:
        print("enter \"1\" to delete at begining of the list")
        print("enter \"2\" to delete at end of the list")
        print("enter \"3\" to delete a specific node")
        print("enter \"4\" to exit")
        c = int(input("enter your choice:"))
        if c==1:
            l.del_beg()
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==2:
            l.del_end()
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==3:
            element = int(input("enter the element to be deleted:"))
            l.del_value(element)
            print(" ")
            print("The linked list in forward traversal is:", end=" ")
            l.forward_traversal()
            print()
            print("The linked list in backward traversal is:", end=" ")
            l.backward_traversal()
            print(" ")
        elif c==4:
            break
        else:
            print(" ")
            print("eneter the correct choice")
    elif choice==3:
        print(" ")
        print("The linked list in forward traversal is:",end=" ")
        l.forward_traversal()
        print()
        print("The linked list in backward traversal is:",end=" ")
        l.backward_traversal()
        print(" ")
    elif choice==4:
        break
    else:
        print(" ")
        print("please enter a correct choice")
