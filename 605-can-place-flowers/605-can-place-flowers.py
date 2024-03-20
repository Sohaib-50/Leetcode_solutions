class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        a = -1
        b = 0
        c = 1

        while b < len(flowerbed) and n > 0:
            if flowerbed[b] == 1:
                b += 2
            else:
                checks = [flowerbed[b]]
                if (b - 1) >= 0:
                    checks.append(flowerbed[b - 1])
                if (b + 1) < len(flowerbed):
                    checks.append(flowerbed[b + 1])
                
                if all((check == 0 for check in checks)):
                    n -= 1
                    b += 2
                else:
                    b += 1
        return n == 0
