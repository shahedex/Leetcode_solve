class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        fin = []
        lefty = -1
        le = len(A)
        for i in range(le):
            if A[i] < 0:
                lefty += 1
        righty = lefty + 1
        while lefty > -1 and righty < le:
            curr = A[righty] * A[righty]
            neg = A[lefty] * A[lefty]
            if curr < neg:
                fin.append(curr)
                righty += 1
            else:
                fin.append(neg)
                lefty -= 1
        while lefty > -1:
            fin.append(A[lefty] * A[lefty])
            lefty -= 1
        while righty < le:
            fin.append(A[righty] * A[righty])
            righty += 1
        return fin
