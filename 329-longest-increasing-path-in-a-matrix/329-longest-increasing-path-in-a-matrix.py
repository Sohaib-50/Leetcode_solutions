class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        l, m = len(matrix), len(matrix[0])
        memo = [[0 for i in range(m)] for j in range(l)]
        max_sofar = float('-inf')
        for row in range(l):
            for col in range(m):
                max_sofar = max(max_sofar, x := self.dfs(matrix, row, col, memo))

        return max_sofar
        
        
    def dfs(self, matrix, row, col, memo):
        if x := memo[row][col]:
            return x
        
        memo[row][col] = 1
        
        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        
        for r, c in neighbors:
            if (r < 0) or (r >= len(matrix)) or (c < 0) or (c >= len(matrix[0])) or (matrix[r][c] <= matrix[row][col]):
                continue
                
            path_len = self.dfs(matrix, r, c, memo)
            memo[row][col] = max(memo[row][col], path_len + 1)
            
        return memo[row][col]