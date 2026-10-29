from collections import Counter

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        limit = max(nums1)

        total = 0
        for b, freq_b in count2.items():
            step = b * k
            for multiple in range(step, limit + 1, step):
                total += freq_b * count1[multiple]
        return total