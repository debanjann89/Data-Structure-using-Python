class LQ:
    def __init__(self,size):
        self.l = [None]*size
        self.front=self.rear=-1
        self.size=size
    def enqueue(self,value):
        if self.rear==self.size-1:
            print("Queue is full!! Can't Enqueue.")
            return
        if self.front==-1:
            self.front=0
        self.rear +=1
        self.l[self.rear]=value
        print(f"{value} Enqueued")
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return None
        removeitem = self.l[self.front]
        self.front +=1
        print(f"Removed Item {removeitem}")
    def peek(self):
        if self.front==-1:
            print("LQ is empty")
            return None
        print("Front value: ",self.l[self.front])
        print("Rear value: ",self.l[self.rear])
    def traverse(self):
        if self.front==-1:
            print("LQ is empty")
        else:
            print("Queue: ",self.l[self.front:self.rear+1])
lq = LQ(5)
lq.enqueue(29)
lq.enqueue(10)
lq.enqueue(50)
lq.enqueue(40)
lq.enqueue(90)
lq.traverse()
lq.dequeue()
lq.traverse()
lq.peek()

