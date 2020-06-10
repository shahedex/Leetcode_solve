class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        finder = 0
        s_len = len(s)
        if s_len < 1:
            return True
        if len(t) < 1:
            return False
        for c in t:
            if c == s[finder]:
                finder += 1
                if finder == s_len:
                    return True
        return False
