class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if 0 in arr and arr.count(0) > 1:
            return True
        for i in arr:
            for j in arr:
                if j == (2*i) and j != 0:
                    return True
        return False
