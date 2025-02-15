class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.count = n

    def find(self, n):
        par = self.parent[n]
        while par != self.parent[par]:
            self.parent[par] = self.parent[self.parent[par]]
            par = self.parent[par]
        return par

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            return False

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
            self.size[par1] += self.size[par2]  
        elif self.rank[par1] < self.rank[par2]:
            self.parent[par1] = par2
            self.size[par2] += self.size[par1] 
        else:
            self.parent[par1] = par2
            self.rank[par2] += 1
            self.size[par2] += self.size[par1] 
            
        self.count -= 1
        return True

    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)

    def component_size(self, node):
        return self.size[self.find(node)]


if __name__ == '__main__':
    uf = UnionFind(8)
    uf.union(1, 2)
    uf.union(1, 5)
    uf.union(6, 5)
    uf.union(7, 3)
    print(uf.find(6))  # Output 2
    print(uf.union(1, 2))  # Output False
    print(uf.same(1, 5))  # Output True
    print(uf.size)  # Output the size of the component containing node 1