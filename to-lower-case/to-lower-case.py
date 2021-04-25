class Solution:
    ## O(n) time, O(n) space?
    def toLowerCase(self, str: str) -> str:
        str = list(str)
        
        for i in range(len(str)):
            if ord(str[i]) in range(65, 91):
                str[i] = chr(ord(str[i]) + 32)
                
        return "".join(str)
    
    
    ## O(n^2) time, O(1) space
#     def toLowerCase(self, str: str) -> str:
        
#         for i in range(len(str)):
#             if ord(str[i]) in range(65, 91):
#                 str = str[:i] + chr(ord(str[i]) + 32) + str[i+1:]
                
#         return str