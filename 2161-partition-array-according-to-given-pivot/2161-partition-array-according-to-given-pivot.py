class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_thans = []
        more_thans = []
        pivot_frequency = 0
        ans = []
        
        for i in nums:
            if i == pivot:
                pivot_frequency += 1
            elif i < pivot:
                less_thans.append(i)
            else:
                more_thans.append(i)
                
                
        for i in less_thans:
            ans.append(i)
        
        for _ in range(pivot_frequency):
            ans.append(pivot)
        
        for i in more_thans:
            ans.append(i)
            
        return ans