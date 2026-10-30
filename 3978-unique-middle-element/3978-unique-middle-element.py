
from collections import Counter

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle_index = len(nums) // 2
        count = Counter(nums)

        if count[nums[middle_index]] == 1:
            return True
        return False
