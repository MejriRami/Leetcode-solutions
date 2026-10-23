from typing import List
from math import inf

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        minimum = inf
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = prefix[i + length] - prefix[i]
                if s > 0:
                    minimum = min(minimum, s)

        return minimum if minimum != inf else -1