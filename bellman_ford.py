from typing import List, Union


class BellmanFord:
    def __init__(self, edge):
        self.edge = edge
        self.n = len(edge)
        self.prev = list(range(self.n))
        self.dist = [float('inf')] * self.n

    def fit(self):
        self.dist[0] = 0
        for _ in range(self.n - 1):
            for source, destination, weight in self.edge:
                tmp = self.dist[source] + weight
                if self.dist[destination] > tmp:
                    self.dist[destination] = tmp
                    self.prev[destination] = source

    def get_path(self, vertex: int) -> List[int]:
        previous = self.prev[vertex]
        path = [vertex]
        while vertex != previous:
            vertex = previous
            previous = self.prev[vertex]
            path.append(vertex)
        return path[::-1]

    def get_distance(self, vertex: int) -> Union[int, float]:
        return self.dist[vertex]

    def is_negative_cycle(self) -> bool:
        for source, destination, weight in self.edge:
            if self.dist[destination] > self.dist[source] + weight:
                return True
        return False
