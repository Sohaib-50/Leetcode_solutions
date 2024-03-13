class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        # Add characters from both words one by one till one or both run out of characters
        p1 = p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            ans += word1[p1]
            ans += word2[p2]
            p1 += 1
            p2 += 1

        # add remaining part of the word that has chars left
        if p1 == len(word1):
            ans += word2[p2:]
        elif p2 == len(word2):
            ans += word1[p1:]

        return ans

