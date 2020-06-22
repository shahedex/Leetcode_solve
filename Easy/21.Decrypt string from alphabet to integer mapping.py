class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphas = {}
        start = 97
        for i in range(1,27):
            alphas[str(i)] = chr(start)
            start += 1
        i = len(s) - 1
        lst = []
        while i >= 0:
            if s[i] != '#':
                lst.append(alphas[s[i]])
                i -= 1
            else:
                lst.append(alphas[s[i-2]+s[i-1]])
                i -= 3
        return ''.join(lst[::-1])
