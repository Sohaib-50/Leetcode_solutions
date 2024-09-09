class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # find first room with a key
        # visit all rooms whose keys are found
        # for each room explore further (dfs)

        stack = [key for key in rooms[0]]
        visited = {0}
        while stack:
            room = stack.pop()
            visited.add(room)
            stack += [key for key in rooms[room] if key not in visited]

        return len(visited) == len(rooms)
            
