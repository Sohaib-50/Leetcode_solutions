class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        if len(s_words) != len(pattern):
            return False
        
        pattern_word_mappings = {}
        word_pattern_mappings = {}
        for i in range(len(pattern)):
            if not(pattern[i] in pattern_word_mappings) and not(s_words[i] in word_pattern_mappings):
                pattern_word_mappings[pattern[i]] = s_words[i]
                word_pattern_mappings[s_words[i]] = pattern[i]
            if pattern[i] in pattern_word_mappings:
                if (pattern_word_mappings[pattern[i]] != s_words[i]):
                    return False
            if s_words[i] in word_pattern_mappings:
                if word_pattern_mappings[s_words[i]] != pattern[i]:
                    return False
                
        return True