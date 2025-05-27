class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
        
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def Insertion(self,value):
        nd = Node(value)
        if self.head == None:
            self.head = nd
            return
        temp=self.head
        while temp.link != None:
             temp=temp.link
        temp.link = nd
    def insert_at_beginning(self,value):
        nd = Node(value)
        if self.head == None:
            self.head = nd
            return
        temp = self.head
        if temp != None:
            self.head = nd
            nd.link = temp
        print(f"Inserted {value} at the beginning of the list.")
        return
    def insert_at_specific_position(self,position,value):
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
            nd.link = self.head
            self.head = nd
            print(f"Inserted {value} at position 0 (beginning)")
            return
        # If inserting at a specific position
        temp = self.head
        index = 0
        while temp.link != None and index < position - 1:
            temp = temp.link
            index += 1
        if index == position - 1:
            nd.link = temp.link
            temp.link = nd
            print(f"Inserted {value} at position {position}")
        else:
            print("Position out of bounds.")
    def insert_at_end(self,value):
        nd = Node(value)
        if self.head == None:
            self.head = nd
            return
        temp = self.head
        while temp.link != None:
            temp = temp.link
        temp.link = nd
        print(f"Inserted {value} at the end of the list.")
        return
    def InsertAfterSpecificNode(self,item,value):
        temp = self.head
        while temp != None:
            if temp.info == item:
                nd = Node(value)
                nd.link = temp.link
                temp.link = nd
                return
            temp=temp.link
        print(f"item'{item}'not found in the list.")
    def DeleteAtSpecificPosition(self,item):
        print("After Node Deletion: ",end=" ")
        temp = self.head
        prev = temp.link
        while temp.info!= item:
            prev = temp
            temp = temp.link
        prev.link=temp.link
        del temp
    def delete_beg(self):
        if self.head == None:
            print("Empty list")
            return
        temp = self.head
        self.head= temp.link
        print("Item deleted",temp.info)
        del temp
    def traverse(self,item):
        temp = self.head
        while temp != None:
            if temp.info==item:
                print(f"Item Found {item}")
                return
            temp=temp.link
        else:
            print(f"Item not Found {item}")
            return
            
        
    def reverse(self):
        print("Reversed Linked List: ")
        prev = None
        current = self.head
        while current != None:
            next = current.link
            current.link = prev
            prev = current
            current = next
        self.head = prev
    def DeleteAtEnd(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        temp = self.head
        while temp.link.link != None:
            temp = temp.link
        print(f"Deleted {temp.info} from the end of the list.")
        temp.link=None
        del temp
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.info, end=" > ")
            temp=temp.link
        print("None")
    def delete_at_specific(self,position):
        if position < 0 :
            print("No negetive position")
            return
        if self.head == None:
            print("EMpty list")
            return
        temp = self.head
        index = 0
        if position == 0:
            self.head = temp .link
            print("deleted at position",index)
            return
        while temp.link != None and index < position-1 :
            temp = temp.link
            index +=1
        if temp is None or temp.link is None:
            print("Invalid position")
            return
        if index == position -1:
            to_delete = temp.link
            print(f"Deleted {to_delete.info} at position {position}")
            temp.link = to_delete.link
            del to_delete
                    
        
ob = SingleLinkedList()
ob.insert_at_beginning(10)
ob.insert_at_beginning(20)
ob.insert_at_beginning(30)
ob.insert_at_end(40)
ob.insert_at_specific_position(0, 25)
ob.display()
ob.delete_at_specific(2)
ob.display()