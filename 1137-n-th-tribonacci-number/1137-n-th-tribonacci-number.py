# class Solution:
#     def tribonacci(self, n: int) -> int:
        
#         memo = {0:0, 1:1, 2:1}

#         def trib(n):
#             if n in memo:
#                 return memo[n]

#             memo[n] = trib(n - 1) + trib(n - 2) + trib(n - 3)
#             return memo[n]

#         return trib(n)


class Solution:
    def tribonacci(self, n: int) -> int:
        
        tribs = [0, 1, 1]

        if n <= 2:
            return tribs[n]

        for i in range(3, n+1):
            tribs = [tribs[1], tribs[2], (tribs[0] + tribs[1] + tribs[2])]

        return tribs[2]
