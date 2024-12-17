from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    
class Tree:
    def maxDepth(self,root):
        if not root:
            return 0
        lHeight = self.maxDepth(root.left)
        rHeight = self.maxDepth(root.right)
        return max(lHeight,rHeight) + 1
    
    def minDepth(self,root):
        if not root:
            return 0
        queue = deque([[root,1]])
        res = []        
        while queue:
            node,depth = queue.popleft()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append([node.left,depth + 1])
            
            if node.right:
                queue.append([node.right,depth + 1])
            
        
        
    
    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

ob1 = Tree()
print("Maximum Depth:", ob1.maxDepth(root))
print("Minimum Depth:", ob1.minDepth(root))
