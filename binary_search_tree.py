class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def preorder(self):
        print(self.key, end = " ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end = " ")
        if self.right:
            self.right.inorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end = " ")
    
    def search(self,data):
        if self.key == data:
            print("Node is found")
        elif self.key > data:
            if self.left.key == data:
                print("Node is found")
            else:
                print("Node is not found")
        else:
            if self.right.key == data:
                print("Node is found")
            else:
                print("Node is not found")
                
            
        
        
        
root = BST(None)
lst = [10,6,3,1,6,98,3,7] 
for i in lst:
    root.insert(i)
print("Preorder") # 10 6 3 1 7 98 
root.preorder() # 10 6 3 1 7 98 
print("\nInorder:") # 1,3,6,7,10,98
root.inorder() # 1,3,6,7,10,98
print("\nPostorder:")  # 1 3 7 6 98 10
root.postorder()  # 1 3 7 6 98 10
print()
root.search(4)



