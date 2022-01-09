class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        wrongs = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                wrongs += 1
        return wrongs