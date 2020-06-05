class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        flag = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[flag], A[i] = A[i], A[flag]
                flag += 1
        return A
