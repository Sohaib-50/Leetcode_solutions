class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        if arr[0] > arr[1]:
            return False
        
        increasing_progress = True
        decreasing_progress = False
        
        for i in range(1, len(arr)):
            current = arr[i]
            prev = arr[i - 1]
            if current == prev:
                return False
            if increasing_progress:
                if current < prev:
                    increasing_progress = False
                    decreasing_progress = True
            else:  # decreasing progress
                if current > prev:
                    return False
                
        return decreasing_progress