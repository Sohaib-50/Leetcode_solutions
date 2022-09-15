class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        
        reversed_right_half = 0
        while x > reversed_right_half:
            reversed_right_half = (reversed_right_half * 10) + (x % 10)
            x //= 10
            
        return (reversed_right_half == x) or (reversed_right_half // 10 == x)