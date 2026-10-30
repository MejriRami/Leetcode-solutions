
from collections import Counter

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)

        if s[0] == str(x):
            return False

        count = Counter(s)

        if count[str(x)] >= 1:
            return True

        return False
