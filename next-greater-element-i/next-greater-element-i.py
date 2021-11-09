class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            num_found = False
            next_greatest = -1
            for j in nums2:
                if j == i:
                    num_found = True
                elif num_found:
                    if j > i:
                        next_greatest = j
                        break
            ans.append(next_greatest)
        return ans

    
    


