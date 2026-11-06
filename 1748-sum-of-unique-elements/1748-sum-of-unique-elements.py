class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        total=0
        s=set(nums)
        for e  in s  :
            if  nums.count(e)==1 :
                total+=e
        return total

        