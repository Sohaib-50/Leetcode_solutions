class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_int = 0  # the integer converted version of s
        for char in s:
            new_int = (ord(char) - 97) + 1  # get position of current alphabet
            if new_int >= 10:
                s_int = (s_int * 100) + new_int
            else:
                s_int = (s_int * 10) + new_int
        
        # perform transformation on s_int k times
        for _ in range(k):
            new_int = 0  # to temporarily hold the transformed number as s_int will keep changing
            while s_int > 0:  # till s_int isn't exhausted
                new_int += s_int % 10  # add number at least significant position
                s_int = s_int // 10  # remove the least significant position number
            s_int = new_int
            
        return s_int
        