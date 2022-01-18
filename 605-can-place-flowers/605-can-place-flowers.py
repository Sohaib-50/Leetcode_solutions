class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        l = len(flowerbed)
        
        if l == 1:
            return flowerbed[0] == 0
        
        i = 0
        while (i < l) and (n > 0):
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i + 1] == 0:
                        n -= 1
                        i += 1
                elif i == l - 1:
                    if flowerbed[i - 1] == 0:
                        n -= 1
                        i += 1
                elif (flowerbed[i + 1] == 0) and (flowerbed[i - 1] == 0):
                    n -= 1
                    i += 1
            i += 1
        return n == 0
                    