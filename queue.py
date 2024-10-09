class Queue:
    def __init__(self):
        self.queue = []

    # Add an element to the queue (enqueue)
    def add(self, value):
        self.queue.append(value)

    # Peek at the front element of the queue without removing it
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    # Remove the front element from the queue (dequeue)
    def remove(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    # Print all elements in the queue
    def printAll(self):
        return self.queue

    # Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0


# Test the queue
q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)

print("All elements after adding:")
print(q.printAll())

q.remove()  # Remove 1
q.remove()  # Remove 2

print("Top element:", q.peek())

print("All elements:")
print(q.printAll())

q.remove()  # Remove 3
q.remove()  # Remove 4
q.remove()  # Remove 5

# Check if the queue is empty
if q.isEmpty():
    print("Queue is empty")
else:
    print("Queue is not empty")
