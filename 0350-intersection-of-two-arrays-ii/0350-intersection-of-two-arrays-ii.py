class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        no_count = {}
        intersection_elements = []
        for i in range(len(nums1)):
            if nums1[i] in no_count:
                no_count[nums1[i]] = no_count.get(nums1[i], 0) + 1
            else:
                no_count[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in no_count and no_count[nums2[i]] != 0:
                no_count[nums2[i]] = no_count.get(nums2[i], 0) - 1
                intersection_elements.append(nums2[i])
        
        return intersection_elements