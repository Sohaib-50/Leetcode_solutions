class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num_started = False
        current = ""
        nums = set()
        for c in word:
            if c.isdigit():
                current += c
                num_started = True
            elif num_started:
                num_started = False
                nums.add(int(current))
                current = ""
                
        if num_started:
            nums.add(int(current))
            
        return len(nums)