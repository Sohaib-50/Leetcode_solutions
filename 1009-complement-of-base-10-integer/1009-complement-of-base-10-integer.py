class Solution:
    def bitwiseComplement(self, n: int) -> int:
        from math import log, floor
        if n == 0:
            return 1
        return n ^ ((2 ** floor(log(n, 2) + 1)) - 1)