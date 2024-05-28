class BIT:
    def __init__(self, length):
        self.n = length
        self.tree = [0] * (length + 1)

    def update(self, i, x):
        while i <= self.n:
            self.tree[i] += x
            i += (i & -i)

    def query(self, i):
        res = 0
        while i >= 1:
            res += self.tree[i]
            i -= (i & -i)
        return res


bit = BIT(4)
bit.update(1, 1)
bit.update(2, 2)
bit.update(3, 3)
bit.update(4, 4)
print(bit.query(4) - bit.query(0))
