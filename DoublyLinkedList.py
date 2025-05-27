class Node:
    def __init__(self,data):
        self.info = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def Insertion(self,value):
        nd = Node(value)
        if self.head == None:
            self.head=nd
            return
        temp = self.head
        while temp.next != None:
            temp=temp.next
        temp.next = nd
        nd.prev = temp
        
    def InsertAfterSpecificNode(self,item,value):
        temp=self.head
        if temp == None:
            nd = Node(value)
            self.head = nd
            print(f"Inserted {value} as the first element.")
            return
        while temp != None:
            if temp.info==item:
                nd = Node(value)
                nd.next=temp.next
                temp.next=nd
                nd.prev=temp
                return
            temp=temp.next
        print(f"item'{item}'not found in the list.")
    def InsertAtSpecificPosition(self,position,value):
        nd = Node(value)
        if position < 0:
            print("Invalid position. Position cannot be negative.")
            return
        if self.head == None:
            if position == 0:
                self.head = nd
                print(f"Inserted {value} at position {position} (empty list)")
                
            else:
                print("Invalid position. List is empty.")
            return
        # If inserting at the beginning
        if position == 0:
            nd.next = self.head
            self.head.prev = nd
            self.head = nd
            print(f"Inserted {value} at position 0 (beginning)")
            return
        #if inserting at a specific position
        temp = self.head
        index = 0
        while temp.next != None and index < position - 1:
            temp = temp.next
            index += 1
        if index < position - 1:
            print("Position out of bounds.")
            return
        nd.next = temp.next
        temp.next = nd
        nd.prev = temp
        print(f"Inserted {value} at position {position}")
    def DeleteAtSpecificPosition(self,item,position):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if position < 0:
            print("Invalid position. Position cannot be negative.")
            return
        temp = self.head
        index = 0
        if position == 0:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            print(f"Deleted {temp.info} from position {position}")
            del temp
            return
        while temp is not None and index < position:
            if index == position - 1:
                if temp.next is None:
                    print("Position out of bounds.")
                    return
                to_delete = temp.next
                temp.next = to_delete.next
                if to_delete.next is not None:
                    to_delete.next.prev = temp
                print(f"Deleted {to_delete.info} from position {position}")
                del to_delete
                return
            temp = temp.next
            index += 1
        print("Position out of bounds.")
    def DeleteAtBeginning(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        temp = self.head
        self.head = temp.next
        if self.head is not None:
            self.head.prev = None
        print(f"Deleted {temp.info} from the beginning of the list.")
        del temp
    def DeleteAtEnd(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        print(f"Deleted {temp.info} from the end of the list.")
        temp.prev.next = None
        del temp
        return
            
    def traverse(self):
        temp=self.head
        print("Doubly Linked List")
        while temp !=None:
            print(temp.info,end="<->")
            temp=temp.next
        print("None")
       
    def ReverseDisplay(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        print("Reverse Linked List")
        while temp != None:
            if temp.prev == None:
                self.head = temp
            print(temp.info,end="<->")
            temp = temp.prev
        print("None")
dll = DoublyLinkedList()
dll.InsertAtSpecificPosition(0, 10)
dll.Insertion(20)
dll.Insertion(30)
dll.Insertion(40)
dll.InsertAtSpecificPosition(2, 50)
dll.traverse()
dll.DeleteAtBeginning()
dll.traverse()
dll.DeleteAtEnd()
dll.traverse()
dll.ReverseDisplay()
        
            
            
        