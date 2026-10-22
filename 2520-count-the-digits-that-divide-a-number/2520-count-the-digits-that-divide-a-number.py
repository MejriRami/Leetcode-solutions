class Solution:
    def countDigits(self, num: int) -> int:
        number = 0
        n = num                      # work on a copy, keep the original num intact
        while n > 0:
            digit = n % 10
            if num % digit == 0:     # check against the ORIGINAL number
                number += 1
            n = n // 10
        return number