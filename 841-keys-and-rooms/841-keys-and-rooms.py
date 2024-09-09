class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # find first room with a key
        # visit all rooms whose keys are found
        # for each room explore further (dfs)

        i = 0
        while (i < len(rooms)) and (len(rooms[i]) == 0):
            i += 1
        if i == len(rooms):
            return False

        stack = [key for key in rooms[i]]
        visited = {i}
        while stack:
            room = stack.pop()
            visited.add(room)
            stack += [key for key in rooms[room] if key not in visited]

        return len(visited) == len(rooms)
            
