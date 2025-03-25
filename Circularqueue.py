class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity 
        self.front = self.rear = -1  
    def enqueue(self, item):
        if self.front ==(self.rear + 1)%self.capacity:
            print("Queue is full. Cannot enqueue.")
            return
        if self.front==-1:
            self.front = self.rear = 0 
        else:
            self.rear = (self.rear + 1) % self.capacity  
        self.queue[self.rear] = item
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        if self.front==-1:
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear: 
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity 
        print(f"Dequeued {item} from the queue.")
        return item

    def peek(self):
        if self.front ==-1:
            print("Queue is empty.")
            return None
        print("Front value: ",self.queue[self.front])
        print("Rear value: ",self.queue[self.rear])

    def display(self):
        if self.front==-1:
            print("Queue is empty.")
            return
        print("Queue elements are:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()



cq = CircularQueue(4)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()

cq.dequeue()
cq.dequeue()
cq.display()

cq.enqueue(60)
cq.enqueue(70)
cq.display()



