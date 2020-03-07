from typing import List, Union


class WarshallFloyd:
    def __init__(self, dist):
        self.dist = dist 
        self.n = len(dist)
        self.prev = [[i] * self.n for i in range(self.n)]

    def fit(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    tmp = self.dist[i][k] + self.dist[k][j]
                    if self.dist[i][j] > tmp:
                        self.dist[i][j] = tmp
                        self.prev[i][j] = self.prev[k][j]

    def get_path(self, source: int, destination: int) -> List[int]:
        vertex = destination
        previous = self.prev[source][vertex]
        path = [vertex]
        while vertex != previous:
            vertex = previous
            previous = self.prev[source][vertex]
            path.append(vertex)
        return path[::-1]

    def get_distance(self, source: int, destination: int) -> Union[int, float]:
        return self.dist[source][destination]

    def is_negative_cycle(self) -> bool:
        for vertex in range(self.n):
            if self.dist[vertex][vertex] < 0:
                return True
        return False
