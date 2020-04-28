class UnionFindTree:
    """Union Find Tree for disjoint-set data structure.

    Args:
        n (int): number of the vertices.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i: int, j: int):
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            if self.rank[ri] < self.rank[rj]:
                self.parent[ri] = rj
            else:
                self.parent[rj] = ri
                if self.rank[ri] == self.rank[rj]:
                    self.rank[ri] += 1

    def is_same(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)
