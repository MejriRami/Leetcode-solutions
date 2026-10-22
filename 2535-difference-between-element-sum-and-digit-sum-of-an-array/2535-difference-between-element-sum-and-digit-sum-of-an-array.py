class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_list = [int(d) for e in nums for d in str(e)]
        digit_sum = sum(digit_list)
        return abs(element_sum - digit_sum)