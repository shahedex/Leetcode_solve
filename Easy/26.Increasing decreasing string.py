from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        lst = list(sorted(set(s)))
        freq = Counter(s)
        ret = []
        counter = 0
        length = len(lst)
        while len(ret) != len(s):
            x = lst[counter]
            if freq[x] != 0:
                ret.append(x)
                freq[x] -= 1
            counter += 1
            if counter == length:
                lst.reverse()
                counter = 0
        return ''.join(ret)
