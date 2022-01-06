class Solution:
    def findComplement(self, num: int) -> int:
        num_binary_digits = floor(log(num, 2) + 1)
        all_ones = (2 ** num_binary_digits) - 1
        return all_ones - num