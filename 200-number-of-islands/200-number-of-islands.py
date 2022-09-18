class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    self.dfs_mark_visited(grid, row, col)
                    
        return islands
        
        
    def dfs_mark_visited(self, grid, row, col):
        
        # Base Case
        if (row < 0) or (row >= len(grid)) or (col < 0) or (col >= len(grid[0])) or (grid[row][col] == "0"):
            return
        
        grid[row][col] = "0"  # mark as visited
        
        # mark all neighbors visited
        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        for neighbor in neighbors:
            self.dfs_mark_visited(grid, neighbor[0], neighbor[1])
            
    
        