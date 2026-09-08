class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_count = {}

        for i in range(len(nums)):
            if nums[i] not in no_count:
                no_count[nums[i]] = 1
            else:
                no_count[nums[i]] = no_count.get(nums[i], 0) + 1
        
        for key, value in no_count.items():
            if value == 1:
                return key

        return -1
