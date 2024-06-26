class RecentCounter:

    def __init__(self):
        self.recent_requests = []
        self.RECENT_LIMIT = 3000

    def ping(self, t: int) -> int:
        # print(f'Call to ping with t = {t}:')
        # print(self.recent_requests)
        self.recent_requests.append(t)

        while self.recent_requests and self.recent_requests[0] < (t - self.RECENT_LIMIT):
            self.recent_requests.pop(0)

        # print(self.recent_requests, "\n")
        return len(self.recent_requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
