class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        if self.length == 0:
            return None

        tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            tail.prev = None
        self.length -= 1
        return tail

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            head.next = None
        self.length -= 1
        return head

    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None

        cur = self.head
        if index <= self.length:
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.length - 1, index, -1):
                cur = cur.prev
        return cur

    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)

        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node

        self.length += 1
        return True

    def remove(self, index) -> Node:
        if self.length == 0 or index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


if __name__ == '__main__':
    doublyLinkedList = DoublyLinkedList(1)
    doublyLinkedList.append(2)
    doublyLinkedList.append(3)
    doublyLinkedList.append(4)
    doublyLinkedList.remove(1)
    doublyLinkedList.print_list()
