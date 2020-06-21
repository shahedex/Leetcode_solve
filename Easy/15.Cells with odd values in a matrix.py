class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        arr = [[0]*m for _ in range(n)]
        odder = 0
        for i,j in indices:
            arr[i] = list(map(lambda x: x+1, arr[i]))
            for r in arr:
                r[j] += 1
        for i in range(n):
            for j in range(m):
                if arr[i][j] % 2 != 0:
                    odder += 1
        return odder
