from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in present]