class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        
        # transpose matrix
        for i in range(l):
            for j in range(i, l):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                print(matrix[j][i], matrix[i][j])
        
        # mirror matrix along y axis
        for row in range(l):
            i = 0
            j = l - 1
            while i < j:
                matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]

                i += 1
                j -= 1