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


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
print(my_tree.contains(12))
