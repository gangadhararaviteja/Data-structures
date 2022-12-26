class bst:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,key):
        if self.data==None:
            self.data=key
            return
        if self.data==key:
            return
        if self.data>key:
            if self.left:
                self.left.insert(key)
            else:
                self.left =bst(key)
        else:
            if self.data<key:
                if self.right:
                    self.right.insert(key)
                else:
                    self.right =bst(key)

    def search(self,key):
        if self.data==key:
            print("the key is found")
        else:
            if self.data>key:
                if self.left:
                    self.left.search(key)
                else:
                    print("the key is not found")
            elif self.data<key:
                if self.right:
                    self.right.search(key)
                else:
                    print("the key is not found")

    def preorder(self):
        print(self.data,end=",")
        if self.left!=None:
            self.left.preorder()
        if self.right!=None:
            self.right.preorder()

    def inorder(self):
        if self.left!=None:
            self.left.inorder()
        print(self.data,end=",")
        if self.right!=None:
            self.right.inorder()

    def postorder(self):
        if self.left!=None:
            self.left.postorder()
        if self.right!=None:
            self.right.postorder()
        print(self.data,end=",")

    def delete(self,key,curr):
        if self.data==None:
            print("the tree is empty,deletion is not possible")

        elif self.data>key:
            if self.left!=None:
                self.left=self.left.delete(key,curr)
            else:
                print("the node is not found to delete")
        elif self.data<key:
            if self.right!=None:
                self.right=self.right.delete(key,curr)
            else:
                print("the node is not foundto delete")

        elif self.data==key:
            if self.left==None:
                temp=self.right
                if key==curr:
                    self.data=temp.data
                    self.left=temp.left
                    self.right=temp.right
                    temp=None
                    return
                self=None
                return temp
            if self.right==None:
                temp=self.left
                if key==curr:
                    self.data=temp.data
                    self.left=temp.left
                    self.right=temp.right
                    temp=None
                    return
                self=None
                return temp
            node=self.right
            while node.left!=None:
                node=node.left
            self.data=node.data
            self.right.delete(node.data,curr)
        return self
    def min(self):
        n=self
        while n.left!=None:
            n=n.left
        print("the smallest node is:",n.data)

    def max(self):
        n=self
        while n.right!=None:
            n=n.right
        print("the largest node is:",n.data)

def count(node):
    if node==None:
        return 0
    return 1+count(node.left)+count(node.right)



root=bst(None)

while True:
    print()
    print("enter \"1\" to insert a node into the binnary tree")
    print("enter \"2\" to delete a node into the binnary tree")
    print("enter \"3\" to search a node in the binnary tree")
    print("enter \"4\" to traverse the binnary tree")
    print("enter \"5\" to find the minimum value of the binnary tree")
    print("enter \"6\" to find the maximum value of the binnary tree")
    print("enter \"7\" to exit")
    print()
    choice=int(input("enter your choice:"))
    print()

    if choice==1:
        element=int(input("enter the element to be inserted:"))
        print()
        root.insert(element)
        print("the preorder raversal is:",end=" ")
        root.preorder()
        print()
        print("the inorder raversal is:",end=" ")
        root.inorder()
        print()
        print("the postorder raversal is:",end=" ")
        root.postorder()
        print()

    elif choice==2:
        if count(root)>1:
            element=int(input("enter the element to be deleted:"))
            print()
            root.delete(element,root.data)
            print("the preorder raversal is:",end=" ")
            root.preorder()
            print()
            print("the inorder raversal is:",end=" ")
            root.inorder()
            print()
            print("the postorder raversal is:",end=" ")
            root.postorder()
            print()
        else:
            print("deletion is not possible as there is only root node")
            print()
    elif choice==3:
        element=int(input("enter the element to be searched:"))
        print()
        root.search(element)
        print()
    elif choice==4:
        print("enter \"1\" for preorder traversal")
        print("enter \"2\" for inorder traversal")
        print("enter \"3\" for postorder traversal")
        print()
        c=int(input("enter your choice:"))
        if c==1:
            print()
            print("the preorder raversal is:",end=" ")
            root.preorder()
            print()
        elif c==2:
            print()
            print("the inorder raversal is:",end=" ")
            root.inorder()
            print()
        elif c==3:
            print()
            print("the postorder raversal is:",end=" ")
            root.postorder()
            print()
        else:
            print("enter correct choice!")
    elif choice==5:
        root.min()
    elif choice==6:
        root.max()
    elif choice==7:
        break
    else:
        print("enter correct choice!")
