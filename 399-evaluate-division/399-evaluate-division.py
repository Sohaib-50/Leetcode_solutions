class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # build graph
        graph = defaultdict(list)
        for i, equation in enumerate(equations):
            src, dest = equation
            value = values[i]

            graph[src].append((dest, value))
            graph[dest].append((src, 1 / value))

        results = []        
        for query in queries:
            src, dest = query

            if (src not in graph) or (dest not in graph):
                results.append(-1)
                continue

            dfs_stack = [(src, 1)]
            solved = False
            visited = set()
            while dfs_stack and not solved:
                current, result_sofar = dfs_stack.pop()
                
                if current in visited:
                    continue

                visited.add(current)

                for edge in graph[current]:
                    neighbor, weight = edge
                    updated_result = result_sofar * weight

                    if neighbor == dest:
                        results.append(updated_result)
                        solved = True
                        break

                    dfs_stack.append((neighbor, updated_result))

            if not solved:
                results.append(-1)

        return results
   
