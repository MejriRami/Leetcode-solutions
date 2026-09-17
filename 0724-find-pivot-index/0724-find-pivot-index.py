class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # Calculate total sum of array
        total_sum = sum(nums)
        
        left_sum = 0
        
        # Iterate through each index
        for i in range(len(nums)):
            # Right sum = Total - Left - Current
            right_sum = total_sum - left_sum - nums[i]
            
            # Check if left and right sums are equal
            if left_sum == right_sum:
                return i
            
            # Update left_sum for next iteration
            left_sum += nums[i]
        
        # No pivot index found
        return -1