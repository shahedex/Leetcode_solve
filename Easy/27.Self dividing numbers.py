class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right+1):
            num = str(i)
            counter = 0
            for n in num:
                if '0' in num:
                    break
                if i % int(n) == 0:
                    counter += 1
            if counter == len(num):
                ret.append(i)
        return ret
