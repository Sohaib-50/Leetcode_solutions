class Solution:
    def toLowerCase(self, str: str) -> str:
        
        for i in range(len(str)):
            if ord(str[i]) in range(65, 91):
                str = str[:i] + chr(ord(str[i]) + 32) + str[i+1:]
                
        return str