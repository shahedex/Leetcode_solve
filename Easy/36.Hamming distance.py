class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x^y
        counter = 0
        while x:
            counter += x & 1
            x >>= 1
        return counter
        
        
# x = f'{x:b}'
# counter = 0
# for c in x:
#     if c == '1':
#         counter += 1
# return counter
