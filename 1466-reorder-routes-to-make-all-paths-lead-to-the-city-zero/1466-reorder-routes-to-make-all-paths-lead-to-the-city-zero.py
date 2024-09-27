class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        neighbors = { city: [] for city in range(n) }

        for src, dest in connections:
            neighbors[src].append(dest)
            neighbors[dest].append(src)
        
        connections = { (x, y) for x, y in connections }

        visited = set()
        reorder_count = 0
        to_make_reachables = [0]
        while to_make_reachables:
            for level_size in range(len(to_make_reachables)):
                node = to_make_reachables.pop(0)
                visited.add(node)

                for neighbor in neighbors[node]:
                    if neighbor in visited:
                        continue

                    if (node, neighbor) in connections:
                        reorder_count += 1

                    to_make_reachables.append(neighbor)

        return reorder_count


        
