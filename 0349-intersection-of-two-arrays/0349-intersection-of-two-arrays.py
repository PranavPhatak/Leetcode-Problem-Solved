class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = list(set(nums1))
        arr2 = list(set(nums2))
        intersection_elements = []
        for i in range(len(arr1)):
            if arr1[i] in arr2:
                intersection_elements.append(arr1[i])
        
        return intersection_elements

