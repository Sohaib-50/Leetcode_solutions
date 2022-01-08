class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        if len(s_words) != len(pattern):
            return False
        
        pattern_word_mappings = {}
        already_mapped_words = set()
        for i in range(len(pattern)):
            if pattern[i] not in pattern_word_mappings:
                if s_words[i] in already_mapped_words:
                    return False
                else:
                    pattern_word_mappings[pattern[i]] = s_words[i]
                    already_mapped_words.add(s_words[i])
            else:
                if pattern_word_mappings[pattern[i]] != s_words[i]:
                    return False
                
        return True