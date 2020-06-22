class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in grid:
            for j in i:
                if j < 0:
                    ret += 1
        return ret
