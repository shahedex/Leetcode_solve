import collections

class RecentCounter:

    def __init__(self):
        self.qu = collections.deque()

    def ping(self, t: int) -> int:
        self.qu.append(t)
        while self.qu[0] < t-3000:
            self.qu.popleft()
        return len(self.qu)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
