"""from typing import List

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d = {}
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1

        total = 0
        for e in d.keys():
            if d[e] % k == 0:
                total += e * d[e]
        return total
        """
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        return sum(e * c for e, c in count.items() if c % k == 0)