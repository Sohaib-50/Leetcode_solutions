class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # Conditions for being close:
        #   1: length not different
        #   2: same unique chars (corresponds to operation 1)
        #   3: same char frequeinces eg if word1 has freqs 1, 3 1, word 2 may have 3, 1, 3 (corresponds to operation 2)

        # check if different lengths
        if len(word1) != len(word2):
            return False

        # check if containing same unique characters
        if set(word1) != set(word2):
            return False

        # count frequency of each character in both words
        frequency_counts_word1 = {}
        for char in word1:
            frequency_counts_word1[char] = frequency_counts_word1.get(char, 0) + 1

        frequency_counts_word2 = {}
        for char in word2:
            frequency_counts_word2[char] = frequency_counts_word2.get(char, 0) + 1

        # check if both words have same char frequencies regardless of the specific characters themselves
        return sorted(frequency_counts_word1.values()) == sorted(frequency_counts_word2.values())
