class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums = nums.copy()
        while nums:
            candidate = max(nums)
            if candidate <= 0:
                return -1
            if -candidate in nums:
                return candidate
            nums.remove(candidate)
        return -1