class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = j = 0
        current = 1
        while (i < len(word1) and j < len(word2)):
            if current == 1:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
                
            current *= -1
        
        if i == len(word1):
            ans.append(word2[j:])  
        elif j == len(word2):
            ans.append(word1[i:])
            
        return "".join(ans)
                