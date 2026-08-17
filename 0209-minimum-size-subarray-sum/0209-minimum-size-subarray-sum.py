class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        min_count = float('inf')
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                min_count = min(min_count, right-left+1)
                window_sum -= nums[left]
                left += 1
        
        if min_count == float('inf'):
            return 0
        else:
            return min_count

