class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
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
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=" ")

    def search(self, data):
        if self.key == data:
            print("Node is found")
        elif self.key > data:
            if self.left and self.left.key == data:
                print("Node is found")
            else:
                print("Node is not found")
        else:
            if self.right and self.right.key == data:
                print("Node is found")
            else:
                print("Node is not found")

    def min_node(self):
        current = self
        while current.left:
            current = current.left
        print("Minimum Node:", current.key)

    def max_node(self):
        current = self
        while current.right:
            current = current.right
        print("Maximum Node:", current.key)

    # Recursive Max Depth
    def max_depth_recursive(self):
        if not self:
            return 0
        left_depth = self.left.max_depth_recursive() if self.left else 0
        right_depth = self.right.max_depth_recursive() if self.right else 0
        return max(left_depth, right_depth) + 1

    # Iterative Max Depth using DFS
    def max_depth_iterative(self):
        if not self:
            return 0
        
        stack = [[self, 1]]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                if node.left:
                    stack.append([node.left, depth + 1])
                if node.right:
                    stack.append([node.right, depth + 1])
        return max_depth


# Test the BST with max depth methods
root = BST(None)
lst = [10, 6, 3, 1, 6, 98, 3, 7]
for i in lst:
    root.insert(i)

print("Preorder:")
root.preorder()
print("\nInorder:")
root.inorder()
print("\nPostorder:")
root.postorder()

print("\nSearching for 4:")
root.search(4)

print("\nMinimum Node:")
root.min_node()

print("\nMaximum Node:")
root.max_node()

# Max Depth (Recursive)
print("\nMax Depth (Recursive):", root.max_depth_recursive())

# Max Depth (Iterative)
print("Max Depth (Iterative):", root.max_depth_iterative())
