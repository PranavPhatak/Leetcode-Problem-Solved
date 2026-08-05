class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = n * ((n+1) / 2)
        expected_sum = 0
        for num in nums:
            expected_sum += num
        
        return int(actual_sum - expected_sum)
        