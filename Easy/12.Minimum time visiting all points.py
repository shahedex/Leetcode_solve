class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ret = 0
        for i in range(len(points)-1):
            current = points[i]
            reach = points[i+1]
            ret += max(abs(current[0]-reach[0]), abs(current[1]-reach[1]))
        return ret
