class Stack:
    def __init__(self,maxsize):
        self.list,self.max,self.top=[],maxsize,-1
    def push(self,value):
        if self.top < self.max -1:
            self.list.append(value)
            self.top +=1
            print(f"Value Pushed: {value}")
        else:
            print("Stack overflow")
    def pop(self):
        if self.top==-1:
            print("Stac underflow")
        else:
            print(f"Value Popped {self.list.pop()}")
            self.top -=1
    def traverse(self):
        print("Elements in Stack: ",self.list)

s=Stack(5)
s.push(10)
s.push(30)
s.push(60)
s.push(20)
s.traverse()
s.pop()
s.traverse()




        