class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        if '6' not in num:
            return int(num)
        num = list(num)
        for d in range(len(num)):
            if num[d] == '6':
                num[d] = '9'
                break
        ret = ''
        for c in num:
            ret += c
        return int(ret)
