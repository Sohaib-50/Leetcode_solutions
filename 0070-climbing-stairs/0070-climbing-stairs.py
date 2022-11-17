class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(steps_sofar):
            if steps_sofar in memo:
                return memo[steps_sofar]
            if steps_sofar == n:
                memo[steps_sofar] = 1
            elif steps_sofar > n:
                memo[steps_sofar] = 0
            else:
                memo[steps_sofar] = dfs(steps_sofar + 1) + dfs(steps_sofar + 2)
            return memo[steps_sofar]
            
        return dfs(1) + dfs(2)  # no. of routes if we take 1 step + no. of routes if we take 2 steps