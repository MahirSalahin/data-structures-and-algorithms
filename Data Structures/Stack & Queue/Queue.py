class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queqe(self) -> None:
        cur = self.first
        while cur is not None:
            print(cur.value)
            cur = cur.next

    def enqueue(self, value) -> None:
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
# my_queue.print_queqe()
my_queue.dequeue()
my_queue.print_queqe()