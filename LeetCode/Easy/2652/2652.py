# Concluído
# Runtime: 72ms
# Memory: 16MB

class Solution:
    def sumOfMultiples(self, n: int, sum=0) -> int:
        for i in range(1, n+1):
            if (i%3==0 or i%5==0 or i%7==0):
                sum += i
        return sum