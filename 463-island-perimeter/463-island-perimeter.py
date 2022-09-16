class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        
        # find first piece of land
        current_loc = (-1, -1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    current_loc = (i, j)
                    break 
        if current_loc == (-1, -1):
            return 0
        
        # print(current_loc)
        return self.dfs(loc=current_loc, perimeter_sofar=0)
    
    def dfs(self, loc, perimeter_sofar):
        self.grid[loc[0]][loc[1]] = -1  # mark as visited
        
        # check in y direction
        for i in (-1, 1):
            new_loc = (loc[0] + i, loc[1])
            # print(new_loc, loc, perimeter_sofar)
            if (not self.inside_grid(new_loc)):
                perimeter_sofar += 1
            elif (self.is_visted(new_loc)):
                continue
            elif self.is_land(new_loc):
                # print("Calling at " + str(new_loc) + ", " + str(perimeter_sofar))
                perimeter_sofar = self.dfs(new_loc, perimeter_sofar)
            else:
                perimeter_sofar += 1
                
        # check in x direction       
        for j in (-1, 1):
            new_loc = (loc[0], loc[1] + j)
            # print(new_loc, loc, perimeter_sofar)
            if (not self.inside_grid(new_loc)):
                perimeter_sofar += 1
            elif (self.is_visted(new_loc)):
                continue
            elif self.is_land(new_loc):
                # print("Calling at " + str(new_loc) + ", " + str(perimeter_sofar))
                perimeter_sofar = self.dfs(new_loc, perimeter_sofar)
            else:
                perimeter_sofar += 1
                
        return perimeter_sofar

    def inside_grid(self, loc):
        i, j = loc
        if (i < 0) or (j < 0) or (i >= len(self.grid)) or (j >= len(self.grid[0])):
            return False
        return True
    
    def is_land(self, loc):
        if self.grid[loc[0]][loc[1]] == 1:
            return True
        return False

    def is_visted(self, loc):
        if self.grid[loc[0]][loc[1]] == -1:
            return True
        return False

            
        
        
        