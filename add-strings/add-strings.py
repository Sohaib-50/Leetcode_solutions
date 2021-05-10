class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for i in num1:
            n1 *= 10
            n1 += ord(i) - 48
            
        for i in num2:
            n2 *= 10
            n2 += ord(i) - 48
        
        return str(n1 + n2)