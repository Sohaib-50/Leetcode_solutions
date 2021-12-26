class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        min_heap = []
        for point in points:
            distance_squared_origin = (point[0] ** 2) + (point[1] ** 2)
            heapq.heappush(min_heap, (distance_squared_origin, point))
            
        return [heapq.heappop(min_heap)[1] for i in range(k)]