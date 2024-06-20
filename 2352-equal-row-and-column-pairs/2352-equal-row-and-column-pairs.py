class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        for i in range(len(grid)):
            row = tuple(grid[i])
            rows[row] = rows.get(row, 0) + 1

        ans = 0

        for col in range(len(grid)):
            column = []
            for row in range(len(grid[0])):
                column.append(grid[row][col])

            column = tuple(column)
            if column in rows:
                ans += rows[column]

        return ans               
