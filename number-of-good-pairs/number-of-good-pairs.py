class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
#         frequencies = {}
#         for index in range(len(nums)):
#             if nums[index] in frequencies:
#                 frequencies[nums[index]] += 1
#             else:
#                 frequencies[nums[index]] = 1
        
#         count = 0
#         for num in frequencies:
#             frequency = frequencies[num]
#             count += ((frequency ** 2) - frequency) //2
    
#         return count
    
        frequency_map = {}
        for i in range(len(nums)):
            if nums[i] in frequency_map:
                frequency_map[nums[i]] += 1
            else:
                frequency_map[nums[i]] = 1

        answer = 0
        for num in frequency_map:
            n = frequency_map[num]
            answer +=  ((n ** 2) - n) //2

        return answer


    
    
# nums = [1, 2, 3, 1, 1, 3]
#         0, 1, 2, 3, 4, 5


# {
#     1 -> 3
#     2 -> 1
#     3 -> 2
# }


# (0, 3)
# (0, 4)
# (3, 4)
# (2, 4)

  
#     3 * 2 // 2
#     6 // 2 
#     3
    
#     2 * 1 // 2
#     2 // 2
#     1















# {
#     1: 3
#     2: 1
#     3: 2
# }

# (n^2 - n) / 2
# 9 - 3 / 2 = 6 / 3 = 3
# 1 - 1 / 2 = 0 / 2 = 0
# 4 - 2 / 2 = 2 / 2 = 1
#                     4 => Answer
    

    
