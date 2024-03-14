class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def is_divisor(s1, s2) -> bool:
            ''' returns True if s2 can be divided by s1, False otherise '''
            return (s1 * (len(s2) // len(s1))) == s2

        possible_gcd = str1 if (len(str1) < len(str2)) else str2

        while len(possible_gcd) > 0 and not (is_divisor(possible_gcd, str1) and is_divisor(possible_gcd, str2)):
            possible_gcd = possible_gcd[:-1]

        return possible_gcd



        '''
        Thinking Process:

        The GCD can't be longer than the shorter string.
        GCD will be prefix of both

        Possible algo 1:
        Find shorter length string
        Find prefix length, starting from full length of shorter one
        If no prefix then no GCD, return empty string
        If prefix found, find
        '''
