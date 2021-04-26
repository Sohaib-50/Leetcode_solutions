class Solution:
    def heightChecker(self, heights: List[int]) -> int:
#         max_sofar = 0
#         ans = 0
#         for height in heights:
#             if height >= max_sofar:
#                 max_sofar = height
#             else:
                
        expected = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
                
        return ans
            