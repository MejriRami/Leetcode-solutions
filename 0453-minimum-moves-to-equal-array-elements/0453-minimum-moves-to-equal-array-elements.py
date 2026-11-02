class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()   
        total=0
        for i  in range (1,len(nums)) :
            total+=abs(nums[i]-nums[0])
        return  total