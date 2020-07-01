class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        csize = len(A[0])
        size = len(A)
        ret = set()
        for i in range(csize):
            is_delete = False
            for j in range(size-1):
                if ord(A[j][i]) > ord(A[j+1][i]):
                    is_delete = True
                    break
            if is_delete:
                ret.add(i)
        return len(ret)
