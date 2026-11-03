class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total=0
        maximum=max(nums)
        for e  in   nums :
            total+=abs(e-maximum)
        return total