class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n + 1):
            n1 = i
            n2 = n - i
            
            if (not ("0" in str(n1))) and (not ("0" in str(n2))):
                return n1, n2