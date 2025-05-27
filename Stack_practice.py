class Stack:
    def __init__(self, max_size):
        self.l = []
        self.max= max_size
        self.top = -1
    def push(self, value):
        if self.top < self.max - 1:
            self.l.append(value)
            self.top += 1
            print(f"Pushed {value}") 
        else:
            print(f"Stack Overflow! Cannot push {value}.")
            
    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
        else:
            print(f"Popped {self.l.pop()}")
            self.top -= 1
    def peek(self):
        if self.top == -1:
            print("Stack is empty!")
        else:
            print("Top Element:", self.l[self.top])
    
    def traverse(self):
        print("Stack:", self.l)

stack = Stack(int(input("Max size: ")))
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)  # This should trigger stack overflow
stack.traverse()
stack.pop()
stack.push(70)
stack.traverse()
stack.peek()




        