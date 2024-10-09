class Stack:
    def __init__(self):
        self.stack = []

    # Push an element to the stack
    def push(self, value):
        self.stack.append(value)
        print(f"{value} pushed to stack")

    # Pop the top element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    # Peek at the top element of the stack without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Print the current state of the stack
    def print_stack(self):
        print(f"Stack: {self.stack}")


# Test the stack implementation
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()

# Peek at the top element
print("Top element:", stack.peek())

# Pop elements and show the state of the stack
print("Popped:", stack.pop())
stack.print_stack()

print("Popped:", stack.pop())
stack.print_stack()

print("Popped:", stack.pop())
stack.print_stack()

# Try popping from an empty stack
print("Popped:", stack.pop())
