class Node:
    def __init__(self,data):
        self.link = None
        self.info = data
class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        if self.top == None:
            print("Stack Underflow")
            return None
        else:
             print("Stack in not Empty")
    def push(self,value):
        nd = Node(value)
        nd.link=self.top
        self.top = nd
        print(f"Pushed {value}")
    def pop(self):
        if self.top == None:
            print("Stack Underflow")
            return None
        popped = self.top.info
        self.top = self.top.link
        print(f"Popped {popped}")
    def peek(self):
        if self.top == None:
            return None
        print("Top Element : ",self.top.info)
    def display(self):
        temp = self.top
        print("Stack: ",end=" ")
        while temp != None:
            print(temp.info, end=" -> ")
            temp=temp.link
        print("None")
ob = Stack()
ob.is_empty()
ob.push(10)
ob.push(20)
ob.push(30)
ob.push(40)
ob.display()
ob.peek()
ob.pop()
ob.display()
ob.peek()