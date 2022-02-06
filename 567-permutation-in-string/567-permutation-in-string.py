class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal_hashmap = [0 for _ in range(26)]
        # making goal hashmap
        for char in s1:
            goal_hashmap[ord(char) - ord('a')] += 1
            
        current_hashmap = [0 for _ in range(26)]
        len_s1 = len(s1)
        end = start = 0
        
        for end in range(len(s2)):
            current_hashmap[ord(s2[end]) - ord('a')] += 1  # icnrement frequency of end of window character in hashmap
            if (end - start + 1) == len_s1:
                if current_hashmap == goal_hashmap:
                    return True
                current_hashmap[ord(s2[start]) - ord('a')] -= 1  # decrement frequency of start of window character in hashmap
                start += 1  # to mantain windo size
        
        return False