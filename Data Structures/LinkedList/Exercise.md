# LinkedList: Interview Questions
## 1. Find the middle.
***Concept : slow, fast pointer*** . Fast pointer advances twice as fast as slow pointer. So, by the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

```py
def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

```
## 2. Has loop
***Concept: slow, fast pointer.*** If there is a loop in the list, the fast pointer will eventually meet the slow pointer
```py
def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
## 3. Remove duplicate
Using another data structure, set. 
Time Complexity: O(n)
```py
def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next
```
Without using another data structure.
Time Complexity : O($n^2$)
```py
def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
```
## 4. Find the kth node from the end.
***Concept: slow, fast pointer*** Initially move the fast pointer k step further. Then move both the slow & fast pointer by one step. As initially fast pointer was on *kth* node and slow was on the beginning, by the time fast pointer reaches the end, slow pointer reaches *(end - k)th* node.
```py
def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow
```
## 5. Reverse between index [m,n]. 
Similar:[Leetcode 92](https://leetcode.com/problems/reverse-linked-list-ii/)
```py
def reverse_between(self, m, n):
        if not self.head:
            return None
 
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
 
        for i in range(m):
            prev = prev.next
        
        current = prev.next
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
 
        self.head = dummy.next

```