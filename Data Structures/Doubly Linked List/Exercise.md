# Doubly Linked List: Interview questions
## 1. Swap the values of the first and last node
```py
    def swap_first_last(self) -> None:
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value
```
## 2. Reverse
```py
    def reverse(self) -> None:
        last = self.tail
        first = self.head
        while last:
            last.value, first.value = first.value, last.value
            last = last.prev
            first = first.next
```
```py
def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head
```
## 3. Is Palindrome
```py
def is_palindrome(self):
        if self.length <= 1:
            return True
        first = self.head
        last = self.tail
        for i in range(self.length // 2):
            if first.value != last.value:
                return False
            first = first.next
            last = last.prev
        return True
```
## 4. Swap Nodes in Pairs
Swap the values of adjacent nodes in the linked list.
```py
def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
 
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
 
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
 
            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
 
            self.head = first_node.next
            prev = first_node
 
        self.head = dummy.next
```