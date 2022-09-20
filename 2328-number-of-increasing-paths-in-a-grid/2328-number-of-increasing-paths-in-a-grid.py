class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs_count_paths(x, y):
            if memo[x][y]:
                return memo[x][y]
    
            memo[x][y] = 1
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for i, j in neighbors:
                if (i < 0) or (j < 0) or (i >= l) or (j >= m) or (grid[i][j] <= grid[x][y]):
                    continue
                else:
                    memo[x][y] += dfs_count_paths(i, j) % mod
            
            return memo[x][y]
                
        
        answer = 0
        l = len(grid)
        m = len(grid[0])
        memo = [[0 for y in range(m)] for x in range(l)]
        mod = ((10**9) + 7)
        for x in range(l):
            for y in range(m):
                answer += dfs_count_paths(x, y)  % mod
                
        return answer % mod