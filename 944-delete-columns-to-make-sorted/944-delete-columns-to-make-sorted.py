class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletions = 0
        for column in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row - 1][column] > strs[row][column]:
                    deletions += 1
                    break
                   
        return deletions