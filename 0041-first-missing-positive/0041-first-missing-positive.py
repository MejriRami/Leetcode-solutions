class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        s = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in s:
                return i