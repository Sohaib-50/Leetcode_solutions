class Solution:
    memo = {0: 1}
    def climbStairs(self, n: int) -> int:

        if n < 0:
            return 0

        if n in Solution.memo:
            return Solution.memo[n]

        Solution.memo[n] = self.climbStairs(n - 1) +  self.climbStairs(n - 2)

        return Solution.memo[n]
