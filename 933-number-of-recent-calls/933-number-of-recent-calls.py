class RecentCounter:

    def __init__(self):
        self.requests = []
        self.top = -1

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.top += 1
        x = self.top
        result = 0
        while self.requests[x] >= (t - 3000) and x >= 0:
            result += 1
            x -= 1
        return result


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
