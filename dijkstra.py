import heapq
from typing import List, Union


class Dijkstra:
    """Dijkstra Algorithm returns the shortest path at positive weighted graph.

    Args:
        edge (List[List[(w, v)]]): adjacent list with the weight.
            w (Union[int, float]): positive weight.
            v (int): the edge's terminal vertex.
    """
    def __init__(self, edge):
        self.edge = edge
        n = len(edge)
        self.prev = list(range(n))
        self.dist = [float('inf')] * n

    def fit(self):
        self.dist[0] = 0
        queue = [(0, 0)]
        while queue:
            _, vertex = heapq.heappop(queue)
            for weight, destination in self.edge[vertex]:
                tmp = self.dist[vertex] + weight
                if self.dist[destination] > tmp:
                    self.dist[destination] = tmp
                    self.prev[destination] = vertex
                    heapq.heappush(queue, (tmp, destination))

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
