class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_area = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 1:  # if current coordinate is a land
                    max_area = max(max_area, j := self.area_of_island_dfs(row, col))
                    
        return max_area
    
    
    def area_of_island_dfs(self, row, col, area_sofar=0):
        # Base case
        if not self.is_land(row, col):
            return area_sofar
        
        area_sofar += 1  # count area of current coordinate
        self.grid[row][col] = 0  # mark as visited
                
        neighbors = [
            (row - 1, col), 
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        for x, y in neighbors:
            area_sofar = self.area_of_island_dfs(x, y, area_sofar)
                
        return area_sofar
    
    def is_land(self, row, col):
        if (row < 0) or (row >= len(self.grid)) or (col < 0) or (col >= len(self.grid[0])) or (self.grid[row][col] == 0):
            return False
        else:
            return True