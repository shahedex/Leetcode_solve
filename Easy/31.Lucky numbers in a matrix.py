class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = []
        ret = []
        for mat in matrix:
            mins.append(min(mat))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j]
                if temp not in mins:
                    continue
                for k in range(len(matrix)):
                    if matrix[k][j] > temp:
                        temp = matrix[k][j]
                if temp == matrix[i][j]:
                    ret.append(temp)
        return ret
