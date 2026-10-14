from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for c in count_t:
            if count_t[c] > count_s[c]:
                return c