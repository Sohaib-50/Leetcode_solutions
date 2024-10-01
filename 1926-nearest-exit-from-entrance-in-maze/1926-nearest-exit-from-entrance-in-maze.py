class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque
        
        def is_valid_coordinate(x, y):
            return (x >= 0) and (y >= 0) and (x < len(maze)) and (y < len(maze[0])) and (maze[x][y] == ".")


        def is_exit(x, y):
            return (maze[x][y] == ".") and ([x, y] != entrance) and (
                x == 0
                or 
                y == 0
                or
                x == len(maze) - 1
                or 
                y == len(maze[0]) - 1
            )

        # queue = deque([entrance])
        queue = [entrance]
        visited = {tuple(entrance)}
        steps = 0
        while queue:

            for i in range(len(queue)):
                # x, y = queue.popleft()
                x, y = queue.pop(0)
                visited.add((x, y))

                # print((x,y), is_exit(x,y), is_valid_coordinate(x,y))
                if is_exit(x, y):
                    return steps

                for change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i, j = (x + change[0], y + change[1])
                    if ((i, j) not in visited) and (is_valid_coordinate(i, j)):
                        visited.add((i, j))
                        queue.append((i, j))
                
                
            steps += 1

        return -1
