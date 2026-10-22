class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        negative = [e for e in nums if e < 0]
        postive = [e for e in nums if e > 0]
        return max(len(postive), len(negative))