class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class CicularLinkedList:
    def __init__(self):
        self.head=None
    def Insertion(self,value):
        nd = Node(value)
        if self.head == None:
            self.head = nd
            self.head.link=self.head
        else:
            temp=self.head
            while temp.link != self.head:
                temp=temp.link
            temp.link = nd
            nd.link=self.head
    def Insert_at_beginning(self,value):
        nd = Node(value)
        if self.head == None:
            self.head = nd
            self.head.link = self.head
        else:
            temp = self.head
            while temp.link != self.head:
                temp = temp.link
            temp.link = nd
            nd.link = self.head
            self.head = nd
            print(f"Inserted {value} at the beginning of the list.")
            return
    def Insert_at_end(self,value):
        nd = Node(value)
        if self.head == None:
            self.head = nd
            self.head.link = self.head
        else:
            temp = self.head
            while temp.link != self.head:
                temp = temp.link
            temp.link = nd
            nd.link = self.head
            print(f"Inserted {value} at the end of the list.")
            return
    def Delete_at_beginning(self):
        if self.head == None:
            print("List is empty. Cannot delete.")
            return
        if self.head.link == self.head:
            print(f"Deleted {self.head.info} from the beginning of the list.")
            self.head = None
            return
        temp = self.head
        last = self.head
        while last.link != self.head:
            last = last.link
        self.head = self.head.link
        last.link = self.head
        print(f"Deleted {temp.info} from the beginning of the list.")
        del temp
    
        print(f"New head is now {self.head.info}.")
        return
    def Delete_at_end(self):
        if self.head == None:
            print("List is empty. Cannot delete.")
            return
        if self.head.link == self.head:
            print(f"Deleted {self.head.info} from the end of the list.")
            self.head = None
            return
        temp = self.head
        while temp.link != self.head:
            prev = temp
            temp = temp.link
        if temp.link == self.head:
            prev.link = temp.link
            print(f"Deleted {temp.info} from the end of the list.")
            del temp
            return
       
    def InsertAtSpecificPosition(self,item,value):
        temp = self.head
        while temp.link != self.head:
            if temp.info == item:
                    nd = Node(value)
                    nd.link = temp.link
                    temp.link = nd
                    return                
            temp=temp.link
        else:
            if temp.info == item:
                nd = Node(value)
                temp.link = nd
                nd.link = self.head       
            else:
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
        
    def traverse(self,item):
        temp = self.head
        while temp.link != None:
            if temp.info != item:
                print(f"Item Not Found {item}")
                break
            else:
                print(f"Item Found {item}")
                break
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.info, end=" > ")
            temp = temp.link
            if temp == self.head:
                break
        if temp == None:
            print("Empty List")
        else:
            
            print(temp.info,"(Back to Head)")
ob = CicularLinkedList()
ob.Insert_at_beginning(10)
ob.Insert_at_beginning(20)
ob.Insert_at_beginning(30)
ob.Insert_at_beginning(40)
ob.Insert_at_beginning(50)
ob.display()
#ob.Delete_at_beginning()
ob.Delete_at_end()
ob.Delete_at_end()
ob.Delete_at_end()
ob.Delete_at_end ()
ob.Delete_at_end()
ob.Delete_at_end()
ob.display()