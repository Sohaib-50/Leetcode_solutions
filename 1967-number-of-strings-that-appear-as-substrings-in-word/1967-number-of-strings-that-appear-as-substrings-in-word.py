class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for x in patterns:
            if x in word:
                count += 1
                
        return count