class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self) -> None:
        cur = self.top
        while cur is not None:
            print(cur.value)
            cur = cur.next


    def push(self, value) -> None:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self) -> Node:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
# my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()