class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    zero_rows.add(x)
                    zero_columns.add(y)
                    
        for row in zero_rows:
            col = 0
            while col < len(matrix[0]):
                matrix[row][col] = 0
                col += 1
        
        for col in zero_columns:
            row = 0
            while row < len(matrix):
                matrix[row][col] = 0
                row += 1
        
#         for x, y in zero_positions:
            
#             # go up
#             temp_x = x - 1
#             while temp_x >= 0:
#                 matrix[temp_x][y] = 0
#                 temp_x -= 1
                
#             # go down
#             temp_x = x + 1
#             while temp_x < len(matrix):
#                 matrix[temp_x][y] = 0
#                 temp_x += 1
                
#             # go left
#             temp_y = y - 1
#             while temp_y >= 0:
#                 matrix[x][temp_y] = 0
#                 temp_y -= 1
                
#             # go right
#             temp_y = y + 1
#             while temp_y < len(matrix[0]):
#                 matrix[x][temp_y] = 0
#                 temp_y += 1