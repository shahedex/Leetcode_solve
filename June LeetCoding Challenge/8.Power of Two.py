class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1 or n == 2:
            return True
        while n > 1:
            n /= 2
        if n == 1:
            return True
        return False
        

# if n < 1:
#     return False
# if n == 1 or n == 2:
#     return True
# elif n % 2 != 0 or (n / 2) % 2 != 0:
#     return False
# else:
#     while n != 2:
#         n /= 2
#         if n % 2 != 0:
#             return False
#     return True
        