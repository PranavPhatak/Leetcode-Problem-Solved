1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        for num in nums:
4            index = abs(num) - 1
5            nums[index] = -abs(nums[index])
6
7        answer = []
8
9        for i in range(len(nums)):
10            if nums[i] > 0:
11                answer.append(i+1)
12        
13        return answer
14        