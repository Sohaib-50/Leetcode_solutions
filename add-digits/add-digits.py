class Solution:
    def addDigits(self, num: int) -> int:
        current = num
        
        while current >= 10:  # not single digit
            new = 0
            while current > 0:
                new += current % 10
                current = current // 10
                
            current = new
            
        return current