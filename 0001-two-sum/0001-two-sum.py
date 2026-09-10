class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            lookup_number = target - nums[i]

            if (lookup_number in map) and (map.get(lookup_number) != i):
                return [i, map.get(lookup_number)]