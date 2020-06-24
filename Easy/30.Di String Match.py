class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        d = len(S)
        i = 0
        ret = []
        for s in S:
            if s == 'I':
                ret.append(i)
                i += 1
            else:
                ret.append(d)
                d -= 1
        if S[-1] == 'I':
            ret.append(i)
        else:
            ret.append(d)
        return ret
