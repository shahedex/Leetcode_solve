class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            print(A)
            return False
        ind = -1
        le = len(A)
        for i in range(le):
            if i+1 < le:
                if A[i] < A[i+1]:
                    ind = i
                else:
                    break
        if ind == -1 or ind >= le-2:
            return False
        else:
            for i in range(ind+1, le):
                if i+1 < le:
                    if A[i] <= A[i+1]:
                        return False
        return True
