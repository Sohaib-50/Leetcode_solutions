class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def manhattan_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        ans = -1
        for i in range(len(points)):
            x2, y2 = points[i]
            if (x == x2) or (y == y2):
                if ans == -1:
                    ans = i
                else:
                    if manhattan_distance(x, y, x2, y2) < manhattan_distance(x, y, points[ans][0], points[ans][1]):
                        ans = i
        return ans
                        