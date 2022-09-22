class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        bfs_queue = [(sr, sc)]
        visited = {(sr, sc)}
        start_color = image[sr][sc]
        
        while bfs_queue:
            current_level_size = len(bfs_queue)
            for i in range(current_level_size):
                row, col = bfs_queue.pop(0)
                image[row][col] = color
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for x, y in neighbors:
                    
                    # if neighbor isn't out of bounds and different color from start pixel and already visited, then add to queue
                    if not ( (x < 0) or (x >= len(image)) or (y < 0) or (y >= len(image[0])) or (image[x][y] != start_color) or ((x, y) in visited) ):
                        bfs_queue.append((x, y))
                        
                    visited.add((x, y))
                        
        return image
                    
        