class Node:
    def __init__(self,data):
        self.info = data
        self.link = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enquee(self,value):
        nd = Node(value)
        if self.front == None:
             self.front = self.rear =nd
             self.rear = self.front
        else:
            self.rear.link = nd
            self.rear = nd
    def dequeue(self):
        temp = self.front
        if self.front==None:
            print("Queue is empty.")
            return None
        self.front=self.front.link
        print("Dequeued Succesfully",temp.info)
    def peek(self,item):
        temp = self.front
        if self.front== None:
            print("Queue is empty.")
            return
        while temp!=None:
            if temp.info == item:
                print(f"Item found {item}")
                return
            temp=temp.link
        else:
            print(f"Item not found {item}")
            
    def display(self):
        temp = self.front
        if temp == None:
            print("Queue is empty")
            return
        while temp!= None:
            print(temp.info, end=" -> ")
            temp = temp.link
        print("None")
ob = Queue()
ob.enquee(10)
ob.enquee(20)
ob.enquee(30)
ob.enquee(40)
ob.display()
ob.dequeue()
ob.display()
ob.peek(300)

    
        
            
            
            
            
            
            
            