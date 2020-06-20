class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x = y = 0
        for c in s:
            if c == 'R':
                x += 1
            else:
                x -= 1
            if x == 0:
                y += 1
        return y
