class Heap:
    def __init__(self) -> None:
        self.heap = [0]

    def __perculate_up(self, id):
        if id <= 1 or self.heap[id] > self.heap[id // 2]:
            return
        self.heap[id], self.heap[id//2] = self.heap[id // 2], self.heap[id]
        self.__perculate_up(id // 2)

    def push(self, val):
        self.heap.append(val)
        self.__perculate_up(len(self.heap) - 1)

    def __perculate_down(self, id):
        if 2 * id >= len(self.heap):
            return

        if 2 * id + 1 >= len(self.heap):
            if self.heap[id] > self.heap[id*2]:
                self.heap[id], self.heap[id*2] = self.heap[id*2], self.heap[id]
            return

        if self.heap[id*2] < self.heap[id*2+1] and self.heap[id*2] < self.heap[id]:
            self.heap[id], self.heap[id*2] = self.heap[id*2], self.heap[id]
            self.__perculate_down(id*2)

        elif self.heap[id*2] > self.heap[id*2+1] and self.heap[id*2+1] < self.heap[id]:
            self.heap[id], self.heap[id*2+1] = self.heap[id*2+1], self.heap[id]
            self.__perculate_down(id*2+1)

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap[1]

        front = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.__perculate_down(1)
        return front

    def top(self):
        if len(self.heap) == 1:
            return None
        return self.heap[1]

    def heapify(self, arr: list):
        arr.append(arr[0])
        self.heap = arr
        mid = (len(arr) - 1) // 2
        for i in range(mid, 0, -1):
            self.__perculate_down(i)


if __name__ == '__main__':
    pq = Heap()
    pq.push(1)
    pq.push(12)
    pq.push(11)
    pq.push(10)
    pq.push(15)
    pq.push(-1)
    print(pq.pop())
    # print(pq.pop())
    # print(pq.pop())
    # print(pq.pop())
    # print(pq.pop())
    # print(pq.pop())
    print(pq.heap)
    pq.heapify([1, 12, 11, 10, 15, -1])
    print(pq.heap)
