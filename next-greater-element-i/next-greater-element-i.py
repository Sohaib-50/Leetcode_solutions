class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatests = {}
        stacc = []
        
        for num in nums2:
            while len(stacc) != 0 and num > stacc[-1]:
                next_greatests[stacc.pop()] = num
            stacc.append(num)
        
        ans = []
        for num in nums1:
            ans.append(next_greatests.get(num, -1))
            
        return ans
