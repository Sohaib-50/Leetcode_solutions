class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        start = 0
        current_window_vowels = 0
        max_vowels = 0
        for end in range(len(s)):
            if s[end] in vowels:
                current_window_vowels += 1

            if end - start + 1 == k:
                max_vowels = max(max_vowels, current_window_vowels)

                # shrink window
                if s[start] in vowels:
                    current_window_vowels -= 1
                start += 1
        return max_vowels

