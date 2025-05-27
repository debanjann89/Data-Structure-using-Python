class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None
class DoublyCircular:
    def __init__(self):
        self.head=None
    def Insertion(self,value):
        nd = Node(value)
        if self.head == None:
            self.head=nd
            self.head.next= self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = nd
            nd.prev = temp
            nd.next=self.head
    def InsertAtSpecificPosition(self,item,value):
        temp = self.head
        while temp.next != self.head:
            if temp.info == item:
                nd = Node(value)
                nd.next = temp.next
                nd.prev = temp
                temp.next = nd
                return
            temp = temp.next
        else:
            if temp.info == item:
                nd = Node(value)
                nd.next = temp.next
                nd.prev = temp
                temp.next = nd
                nd.next= self.head
            else:
                print(f"item'{item}'not found in the list.")
    def DeleteAtSpecificPosition(self, item):
        print("After Node Deletion: ", end="\n")
        if self.head is None:
            print("The list is empty.")
            return

        temp = self.head
        while True:
            if temp.info == item:
                if temp.next == temp and temp.prev == temp:
                    self.head = None
                    return
                if temp == self.head:
                    self.head = temp.next
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Item '{item}' not found in the list.")
                
    def display(self):
        temp = self.head
        print("Double Circular Linked List: ", end="\n")
        while temp != None:
            print(temp.info, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print(temp.info,"(Back to Head)")
ob = DoublyCircular()
ob.Insertion(10)
ob.Insertion(20)
ob.Insertion(40)
ob.Insertion(60)
ob.InsertAtSpecificPosition(60, 30)
ob.display()
ob.DeleteAtSpecificPosition(60)
ob.display()