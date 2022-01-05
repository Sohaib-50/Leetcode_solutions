class Solution:
    def binaryGap(self, n: int) -> int:
        i = 0
        last_one_idx = -1
        max_gap = 0
        while (n >> i) != 0:
            if ((n >> i) & 1) == 1:
                if last_one_idx >= 0:
                    max_gap = max(max_gap, i - last_one_idx)
                last_one_idx = i
            i += 1
        return max_gap
#         max_gap = 0
#         current_gap = 0
#         # ones_in_progress = False
#         last_num = 0
#         while n:
#             # if (n & 1) == 1:  # last digit is 1
#             #     if not ones_in_progress:
#             #         ones_in_progress = True
#             #     else:
#             #         # distance_so_far = 1
#             # else:  # last digit is 0
#             #     if ones_in_progress:
#             #         ones_in_progress = False
            
#             if (n & 1) == 1:
#                 if last_num == 0:
#                     current_gap += 1
#                     max_gap = max(current_gap, max_gap)
#                     current_gap = 0
#                 else:
#                     current_gap = 1
#             elif current_gap or last_num == 1:  # if current 0 AND one encountered previously
#                 current_gap += 1
            
#             last_num = n & 1        
#             n = n >> 1
            
#         return max_gap

                