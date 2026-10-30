
from math import sqrt

class Solution:
    def isThree(self, n: int) -> bool:
        numberofdivisors = 0

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                if i == n // i:
                    numberofdivisors += 1
                else:
                    numberofdivisors += 2

        return numberofdivisors == 3
