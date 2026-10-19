class Solution:
    def removeZeros(self, n: int) -> int:
        power = 1
        result = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                result += digit * power
                power *= 10
            n //= 10
        return result