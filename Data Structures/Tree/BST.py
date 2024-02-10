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
        if value < current_node.value:
            current_node.right = self._r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        self._r_insert(self.root, value)

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
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root -> Left:', my_tree.root.left.value)        
print('Root -> Right:', my_tree.root.right.value)    



"""
    EXPECTED OUTPUT:
    ----------------
	Root: 2
	Root -> Left: 1
	Root -> Right: 3

"""
