from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        l = list(count.values())
        s = set(l)

        if len(s) == 1:
            # Either every letter appears once (remove any one),
            # or there's only one distinct letter (e.g. "aaaa")
            return l[0] == 1 or len(l) == 1

        if len(s) >= 3:
            return False

        # len(s) == 2
        a, b = sorted(s)  # a < b
        # Case 1: one letter appears exactly once; remove it entirely
        if a == 1 and l.count(a) == 1:
            return True
        # Case 2: one letter appears one more time than the rest; remove one copy
        if b == a + 1 and l.count(b) == 1:
            return True
        return False