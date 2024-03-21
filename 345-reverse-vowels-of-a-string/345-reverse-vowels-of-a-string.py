class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = len(s) - 1
        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            if left_char in vowels and right_char in vowels:
                # swap
                s = s[:left] + s[right] + s[left + 1:right] + s[left] + s[right + 1:]
                left += 1
                right -= 1

            else:
                if left_char not in vowels:
                    left += 1
                if right_char not in vowels:
                    right -= 1

        return s
