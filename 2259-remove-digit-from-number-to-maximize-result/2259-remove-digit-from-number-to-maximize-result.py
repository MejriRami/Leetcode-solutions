class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_val = 0
        for i, c in enumerate(number):
            if c == digit:
                s1 = number[:i] + number[i + 1:]
                max_val = max(max_val, int(s1))
        return str(max_val)