class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        
        for i in range(len(words) - 1):
            
            for j in range(i + 1, len(words)):
                
                eligible = True
                for char in words[i]:
                    if char in words[j]:
                        eligible = False
                
                if eligible:
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans
                