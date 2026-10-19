from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        power = 1
        while n > 0:
            digit = n % 10
            if digit != 0:
                result.append(digit * power)
            n //= 10
            power *= 10
        return result[::-1]