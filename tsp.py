class TSP:
    """Traveling Salesman Problem

    Args:
        distance (List[List[Num]]): distance

    """
    def __init__(self, distance):
        self.distance = distance
        self.n = len(distance)
        self.inf = float('inf')
        self.dp = [[self.inf] * (self.n-1) for _ in range(1 << self.n-1)]
        self.prev = [[-1] * (self.n-1) for _ in range(1 << self.n-1)]

    def fit(self):
        for bit in range(1, 1 << self.n-1):
            for i in range(self.n-1):
                mask = 1 << i
                if bit == mask:
                    self.dp[bit][i] = self.distance[self.n-1][i]
                    self.prev[bit][i] = self.n-1
                elif bit & mask:
                    sub_bit = bit ^ mask
                    for j in range(self.n-1):
                        tmp = self.dp[sub_bit][j] + self.distance[j][i]
                        if tmp < self.dp[bit][i]:
                            self.dp[bit][i] = tmp
                            self.prev[bit][i] = j
        for i in range(self.n-1):
            tmp = self.dp[-1][i] + self.distance[i][self.n-1]
            if tmp < self.dp[0][0]:
                self.dp[0][0] = tmp
                self.prev[0][0] = i

    def get_path(self):
        path = [self.n-1, self.prev[0][0]]
        bit = (1 << self.n-1) - 1
        for _ in range(self.n-1):
            path.append(self.prev[bit][path[-1]])
            if path[-1] == -1:
                return None
            bit ^= 1 << path[-2]
        return path[::-1]

    def get_distance(self):
        return self.dp[0][0]
