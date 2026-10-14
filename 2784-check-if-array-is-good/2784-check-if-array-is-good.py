class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        number_of_n = nums.count(n)
        if number_of_n != 2:
            return False
        else:
            return set(nums) == set(range(1, n + 1))