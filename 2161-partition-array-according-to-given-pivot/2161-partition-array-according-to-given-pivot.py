class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_frequency = 0
        ans = []
        
        for i in nums:
            if i == pivot:
                pivot_frequency += 1
            elif i < pivot:
                ans.append(i)

        for _ in range(pivot_frequency):
            ans.append(pivot)
        
        for i in nums:
            if i > pivot:
                ans.append(i)
            
        return ans