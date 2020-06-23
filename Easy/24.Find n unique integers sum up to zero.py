class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        ret = []
        for i in range(n-1):
            ret.append(i)
        ret.append(sum(ret)*-1)
        return ret
