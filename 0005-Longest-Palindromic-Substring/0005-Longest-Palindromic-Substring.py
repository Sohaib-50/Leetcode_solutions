class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_palindrome(left, right):
            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                left -= 1
                right += 1

            return s[left + 1 : right]


        longest = ""
        for i in range(len(s)):
            # try making palindrome of odd length
            p = expand_palindrome(i, i)
            if len(p) > len(longest):
                longest = p

            # try making palindrome of even length
            p = expand_palindrome(i, i + 1)
            if len(p) > len(longest):
                longest = p

        return longest
