class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x, y, memo):
            ## Base Cases
            # result memo available
            if (x, y) in memo:
                return memo[x, y]
            
            # reached bottom right
            if (x == m - 1) and (y == n - 1):
                memo[x, y] = 1

            # rent out of bounds
            elif (x >= m) or (y >= n):
                memo[x, y] = 0
                
            # recursion
            else:
                memo[x, y] = dfs(x + 1, y, memo) + dfs(x, y + 1, memo)
            
            return memo[x, y]
        
        return dfs(x=0, y=0, memo={})
    
   