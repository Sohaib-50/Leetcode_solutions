class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection1 = set()
        
        for i in nums1:
            intersection1.add(i)
        
        intersection2 = set()
        for i in nums2:
            if i in intersection1:
                intersection2.add(i)
                
        return intersection2