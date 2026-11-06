class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        for bit in range(31):
            count = 0
            for num in nums:
                if num & (2 ** bit) == 2 ** bit:
                    count += 1
            if count >= k:
                result += 2 ** bit
        return result