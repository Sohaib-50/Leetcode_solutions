class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join([char for substring in word1 for char in substring]) == "".join([char for substring in word2 for char in substring])
