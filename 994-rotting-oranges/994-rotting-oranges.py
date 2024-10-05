class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def valid_coordinate(coordinate):
            x, y = coordinate
            return (x >= 0) and (y >= 0) and (x < len(grid)) and (y < len(grid[0]))

        # ans = [[float('inf') for col in range(len(grid[0]))] for row in range(len(grid))]
        queue = []
        freshs = set()
        # visited = set()

        # find all rottens
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    # visited.add((row, col))
                elif grid[row][col] == 1:
                    freshs.add((row, col))

        minutes = 0
        while queue and freshs:

            for _ in range(len(queue)):
                current = queue.pop(0)

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = (current[0] + dx, current[1] + dy)
                    if valid_coordinate((x, y)) and (grid[x][y] == 1):
                        grid[x][y] = 2
                        queue.append((x, y))
                        freshs.remove((x, y))
            minutes += 1
                    
        return minutes if (len(freshs) == 0) else -1
                    

        
