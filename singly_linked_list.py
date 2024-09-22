class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.next
    # Insert new node
    
    def insertAtTheBeginning(self,data):
        newNode = Node(data) # newNode.data -> 10, newNode.next -> None
        newNode.next = self.head # newNode.next -> None
        self.head = newNode # newNode.head -> newNode's address

    
    def insertAtTheEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            node = self.head
            while node.next is not None: # Use node.next is None because we need that last node, use node is None for others
                node = node.next
            node.next = newNode
    
    
    def insertAfter(self,data,x):
        node = self.head
        while node is not None:
            if node.data == x:
                break
            node = node.next
        if node is None:
            print("Node is not present in the LinkedList")
        else:
            newNode = Node(data)
            newNode.next = node.next
            node.next = newNode
    
    def insertBefore(self,data,x):
        node = self.head
        while node is not None:
            if node.data == x:
                break
            prevNode = node
            node = node.next
        if node is None:
            print("Node is not present in the LinkedList")
        else:
            newNode = Node(data)
            prevNode.next = newNode
            newNode.next = node
        
    # Delete node
        
    def deleteAtTheBeginning(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            self.head = self.head.next

    
    def deleteAtTheEnd(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None # Check if only one element is there then make the 
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None
            
    def deleteByValue(self,data):
        node = self.head
        if node is None:
            print("Node is not present in the LinkedList")
        elif node.data == data:
            self.head = None
        else:
            while node is not None:
                if node.data == data:
                    prevNode.next = node.next
                prevNode = node
                node = node.next

    
            


linkedList = LinkedList()
linkedList.insertAtTheBeginning(10)
linkedList.insertAtTheBeginning(20)
linkedList.insertAtTheBeginning(30)
linkedList.insertAtTheEnd(40)
linkedList.insertAfter(50,20)
linkedList.insertBefore(100,40)
print("LinkedList Before Deletion:")
linkedList.printLinkedList()
# linkedList.deleteAtTheBeginning()

# print("linkedList After Deletion:")
# linkedList.printLinkedList()

# linkedList.deleteAtTheEnd()
# print("linkedList After Deletion at the End:")
# linkedList.printLinkedList()

linkedList.deleteByValue(20)
print("linkedList After Deleting Value 20:")
linkedList.printLinkedList()
