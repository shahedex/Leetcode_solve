class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        N = length // 2
        costs = sorted(costs, key=lambda sublist: abs(sublist[0] - sublist[1]))
        ca = 0
        cb = 0
        total = 0
        for i in range(length - 1, -1, -1):
            if (costs[i][0] <= costs[i][1] and ca < N) or cb == N:
                total += costs[i][0]
                ca += 1
            else:
                total += costs[i][1]
                cb += 1
        return total

