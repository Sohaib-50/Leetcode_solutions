class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        for i in nums1:
            set1.add(i)
        
        set2 = set()
        for i in nums2:
            if i in set1:
                set2.add(i)
                
        return set2