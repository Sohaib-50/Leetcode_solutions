class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        l = len(mat)
        for i in range(l):
            ans += mat[i][i] + mat[i][l - 1  - i]
        
        # subtract middle element if odd length matrix (in which case middle element overlaps in rows)
        return ans - mat[l//2][l//2] if l % 2 != 0 else ans  # subtract middle element if 