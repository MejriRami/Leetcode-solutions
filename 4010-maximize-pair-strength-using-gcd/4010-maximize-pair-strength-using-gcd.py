from math import gcd

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        vals = list(set(nums))   # duplicates only ever give strength 1
        if len(vals) == 1:
            return 1
        best = 1
        n = len(vals)
        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(vals[i], vals[j])
                best = max(best, (vals[i] // g) * (vals[j] // g))
        return best