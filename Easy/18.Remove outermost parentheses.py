class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        lis = []
        l = 0
        r = 0
        lst = 0
        for i in range(len(S)):
            if S[i] == '(':
                l += 1
            else:
                r += 1
            lis.append(S[i])
            if l == r:
                lis[lst] = lis[-1] = 0
                l = r = 0
                lst = i+1
        ret = ''
        for i in lis:
            if i != 0:
                ret += i
        return ret
