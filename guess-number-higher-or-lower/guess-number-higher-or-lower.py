# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while True:
            mid = (low + high) // 2
            x = guess(mid)
            if x == 1:
                low = mid + 1
            elif x == -1:
                high = mid - 1
            else:
                break
        return mid