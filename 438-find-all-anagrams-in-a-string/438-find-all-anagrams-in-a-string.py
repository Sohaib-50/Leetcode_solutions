class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram_indices = []
        goal_hashmap = [0 for _ in range(26)]
        current_hashmap = [0 for _ in range(26)]
        end = start = 0
        len_p = len(p)
        
        # make goal hashmap
        for char in p:
            goal_hashmap[ord(char) - ord("a")] += 1
            
        
        for end in range(len(s)):
            # current_char = s[end]
            current_hashmap[ord(s[end]) - ord("a")] += 1  # increment window start char in hashmap
            if (end - start + 1) == len_p:
                if current_hashmap == goal_hashmap:
                    anagram_indices.append(start)
                current_hashmap[ord(s[start]) - ord("a")] -= 1  # decrement window start char from hashmap
                start += 1

        return anagram_indices