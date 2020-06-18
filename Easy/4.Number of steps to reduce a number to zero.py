class Solution:
    def numberOfSteps (self, num: int) -> int:
        num = f'{num:b}'
        return num.count('1') * 2 + num.count('0') - 1
             
# counter = 0
# while num != 0:
#     if num % 2 == 0:
#         num /= 2
#     else:
#         num -= 1
#     counter += 1
# return counter
