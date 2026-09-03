class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
            
        nums.reverse()
        self.reverse_subarray(nums, 0, k-1)
        self.reverse_subarray(nums, k, len(nums)-1)
    
    def reverse_subarray(self, nums: list[int], start: int, end: int) -> None:
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

