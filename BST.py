class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.info = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        nd = Node(value)
        if self.root is None:
            self.root = nd
            return
        temp = self.root
        par = temp
        while temp is not None:
            if value < temp.info:
                par = temp
                temp = temp.left
            elif value > temp.info:
                par = temp
                temp = temp.right
            else:
                print("Repeated value")
                return
        if value < par.info:
            par.left = nd
        else:
            par.right = nd
        print("Inserted value:", value)
        return

    def Search(self, item):
        temp = self.root
        par = None  # Initialize parent to None
        while temp is not None:
            if item < temp.info:
                par = temp
                temp = temp.left
            elif item > temp.info:
                par = temp
                temp = temp.right
            else:
                break
        if temp is not None:
            print(f"Item found: {item}")
        else:
            print(f"Item not found: {item}")
        return temp, par

    def delete(self, item):
        temp, par = self.Search(item)
        if temp is None:
            print("Item not found, cannot delete.")
            return
        else:
            if temp.left is None and temp.right is None:
                self._delete_zero_child(temp, par)
            elif temp.left is not None and temp.right is None:
                self._delete_left_child(temp, par)
            elif temp.left is None and temp.right is not None:
                self._delete_right_child(temp, par)
            else:
                self._delete_both_child(temp, par)
            print(f"Deleted item: {item}")

    def _delete_zero_child(self, temp, par):
        if par is None:  # Deleting the root
            self.root = None
        elif temp.info < par.info:
            par.left = None
        else:
            par.right = None
        del temp

    def _delete_left_child(self, temp, par):
        if par is None:  # Deleting the root
            self.root = temp.left
        elif temp.info < par.info:
            par.left = temp.left
        else:
            par.right = temp.left
        del temp

    def _delete_right_child(self, temp, par):
        if par is None:  # Deleting the root
            self.root = temp.right
        elif temp.info < par.info:
            par.left = temp.right
        else:
            par.right = temp.right
        del temp

    def _delete_both_child(self, temp, par):
        successor = temp.right
        succ_par = temp
        while successor.left is not None:
            succ_par = successor
            successor = successor.left
        temp.info = successor.info  # Replace the deleted node's value with the successor's
        # Now delete the successor (which has at most one right child)
        if succ_par.left == successor:
            succ_par.left = successor.right
        else:
            succ_par.right = successor.right
        del successor

    def inorder(self):
        def _inorder_recursive(node):
            if node is not None:
                _inorder_recursive(node.left)
                print(node.info, end=" ")
                _inorder_recursive(node.right)
        _inorder_recursive(self.root)
        print()

    def preorder(self):
        def _preorder_recursive(node):
            if node is not None:
                print(node.info, end=" ")
                _preorder_recursive(node.left)
                _preorder_recursive(node.right)
        _preorder_recursive(self.root)
        print()

    def postorder(self):
        def _postorder_recursive(node):
            if node is not None:
                _postorder_recursive(node.left)
                _postorder_recursive(node.right)
                print(node.info, end=" ")
        _postorder_recursive(self.root)
        print()

    def display(self):
        self.inorder()  # Inorder traversal gives a sorted view of the BST

b = BST()
b.insert(100)
b.insert(50)
b.insert(90)
b.insert(200)
b.insert(150)
b.insert(60)
b.insert(120)
b.insert(80)
b.insert(180)
b.insert(35)
print("Initial BST:")
b.display()

print("\nSearching for 90:")
b.Search(90)
print("\nSearching for 110:")
b.Search(110)

print("\nInorder traversal:")
b.inorder()
print("\nPreorder traversal:")
b.preorder()
print("\nPostorder traversal:")
b.postorder()

print("\nDeleting 50:")
b.delete(50)
print("BST after deleting 50:")
b.display()

print("\nDeleting 200:")
b.delete(200)
print("BST after deleting 200:")
b.display()

print("\nDeleting 100 (root):")
b.delete(100)
print("BST after deleting 100:")
b.display()
