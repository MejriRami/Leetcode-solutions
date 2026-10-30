
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x1 = x
        sum = 0

        while x1 >= 10:
            sum += x1 % 10
            x1 = x1 // 10

        sum += x1

        if x % sum == 0:
            return sum
        return -1

