"""class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        maximum = float('-inf')
        k, l = -1, -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target and nums[i] != nums[j]:
                    product = nums[i] * nums[j]
                    if product > maximum:
                        maximum = product
                        if nums[i] > nums[j]:
                            k, l = i, j
                        else:
                            k, l = j, i
        return [k, l]"""


class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = i          # remember one index for each value

        best = float('-inf')
        ans = [-1, -1]
        for x in pos:
            y = target - x
            if y in pos and x > y:
                if x * y > best:
                    best = x * y
                    ans = [pos[x], pos[y]]
        return ans