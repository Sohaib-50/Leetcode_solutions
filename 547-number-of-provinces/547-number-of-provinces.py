class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        count_cities = len(isConnected)
        count_provinces = 0

        def bfs(city):
            queue = [city]
            while queue:
                current_city = queue.pop()
                isConnected[current_city][current_city] = 2
                
                for connected_city in range(count_cities):
                    if isConnected[current_city][connected_city] == 1:
                        isConnected[current_city][connected_city] = 2
                        isConnected[connected_city][current_city] = 2
                        queue.append(connected_city)
            
        for city in range(count_cities):
            for connected_city in range(count_cities):
                if isConnected[city][connected_city] == 1:
                    count_provinces += 1
                    bfs(city)
                    # print("\n".join((str(row) for row in isConnected)))
                    # print()
 
        return count_provinces

