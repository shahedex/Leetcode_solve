class Solution:
    def fib_generator(self,N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib_generator(N - 1) + self.fib_generator(N - 2)
    
    def fib(self, N: int) -> int:
        return self.fib_generator(N)
