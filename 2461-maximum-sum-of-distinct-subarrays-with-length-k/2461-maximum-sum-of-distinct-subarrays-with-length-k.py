class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        window_sum = 0
        window = {}
        for i in range(k):
            window[nums[i]] = window.get(nums[i], 0) + 1
            window_sum += nums[i]
        
        if len(window) == k:
            max_sum = window_sum

        for i in range(k, len(nums)):
            left = nums[i-k]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            right = nums[i]
            window[right] = window.get(nums[i], 0) + 1

            window_sum += right - left

            if len(window) == k:
                max_sum = max(max_sum, window_sum)
            
        return max_sum


        