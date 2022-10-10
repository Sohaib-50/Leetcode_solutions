class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        
        while (left <= right) and (bottom >= top):
            
            # move right 
            for i in range(left, right + 1):
                # print(row, col)
                answer.append(matrix[top][i])
            top += 1  # adjust top boundary
            
            # move down
            for i in range(top, bottom + 1):
                # print(row, col)
                answer.append(matrix[i][right])
            right -= 1  # adjust right boundary
            
            if not ((left <= right) and (bottom >= top)):
                break
                
            # move left
            for i in range(right, left - 1, -1):
                # print(row, col)
                answer.append(matrix[bottom][i])
            bottom -= 1
                
            # move up
            for i in range(bottom, top - 1, -1):
                # print(row, col)
                answer.append(matrix[i][left])
            left += 1
                
            
            
        return answer
                
            