class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # to avoid duplicate triplets
            if (i > 0) and (nums[i] == nums[i - 1]):
                continue
                
            remaining = -nums[i]
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == remaining:
                    answer.append([nums[i], nums[low], nums[high]])
                    
                    # to avoid duplicates
                    while (low < high) and (nums[low] == nums[low + 1]):
                        low += 1
                    while (low < high) and (nums[high] == nums[high - 1]):
                        high -= 1
                        
                    low += 1
                    high -= 1

                elif nums[low] + nums[high] < remaining:
                    low += 1
                else:
                    high -= 1
                    
        return answer
        