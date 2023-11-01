class Stack():

    # Constructor
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty() == 0:
            self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return print("Stack is empty")

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return 0
        else:
            return 1

    def showStack(self):
        for element in self.stack:
            print(element)


if __name__ == "__main__":
    Stack_A = Stack()

    for i in range(0, 6):
        Stack_A.push(i)
    print("Elementos insertados")

    Stack_A.pop()
    Stack_A.pop()

    Stack_A.showStack()
