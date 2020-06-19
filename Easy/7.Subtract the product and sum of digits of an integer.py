class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mul = 1
        while n != 0:
            x = n % 10
            sum += x
            mul *= x
            n = int(n/10)
        return mul - sum
