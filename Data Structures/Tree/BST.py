class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        cur = self.root
        while True:
            if new_node.value == cur.value:
                return False
            if new_node.value < cur.value:
                if cur.left is None:
                    cur.left = new_node
                    return True
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new_node
                    return True
                cur = cur.right

    def contains(self, value) -> bool:
        cur = self.root
        while cur is not None:
            if cur.value == value:
                return True
            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return False

    # implementing all function recursively
    def _r_contains(self, current_node, value) -> bool:
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self._r_contains(current_node.left, value)
        if value > current_node.value:
            return self._r_contains(current_node.right, value)

    def r_contains(self, value) -> bool:
        return self._r_contains(self.root, value)

    def _r_insert(self, current_node, value) -> Node:
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self._r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self._r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        self._r_insert(self.root, value)



    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    

    def _delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left = self._delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                current_node = None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                inorder_successor = self.min_value(current_node.right)
                current_node.value = inorder_successor
                current_node.right = self._delete_node(current_node.right, inorder_successor)
        return current_node

    def delete_node(self, value)-> Node:
        self._delete_node(self.root, value)

# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# # print(my_tree.root.value)
# # print(my_tree.root.left.value)
# # print(my_tree.root.right.value)
# print(my_tree.contains(12))

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
       2
      / \
     1   3
"""

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)


my_tree.delete_node(2)

"""
       3
      / \
     1   None
"""


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)



"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""