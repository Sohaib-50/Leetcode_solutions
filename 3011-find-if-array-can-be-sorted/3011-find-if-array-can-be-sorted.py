class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        current_set_bits = bin(nums[0]).count("1")
        current_max = nums[0]
        current_min = nums[0]
        previous_max = float('-inf')

        for i in range(1, len(nums)):
            n = nums[i]

            if bin(n).count("1") != current_set_bits:
                if current_min < previous_max:
                    print(i, current_min, previous_max)
                    return False
                print("break on", i)
                current_set_bits = bin(n).count("1")
                previous_max = current_max
                current_min = n
                current_max = n
                

            else:
                
                current_min = min(current_min, n)
                current_max = max(current_max, n)
        
        print(current_min, previous_max)
        return current_min >= previous_max   
