class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        s = set(nums)
        for e in s:
            if nums.count(e) == len(nums) // 2:
                return e