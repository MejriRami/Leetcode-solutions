class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        candidate = max(sum(nums) // len(nums) + 1, 1)
        seen = set(nums)
        while candidate in seen:
            candidate += 1
        return candidate