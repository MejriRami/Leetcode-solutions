from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        negative = bisect_left(nums, 0)               # count of elements < 0
        postive = len(nums) - bisect_right(nums, 0)   # count of elements > 0
        return max(postive, negative)