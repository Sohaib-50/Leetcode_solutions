# https://leetcode.com/problems/decode-string/solutions/4717135/100-step-by-step-explaination-with-pictures-optimized-stack-approach/
        
class Solution:
    def decodeString(self, s: str) -> str:

        repeat_counts_stack = []
        patterns_stack = []
        current_repeat_count = 0
        current_pattern = ""

        for char in s:
            print(char, repeat_counts_stack, patterns_stack, current_pattern)

            if char.isdigit():
                current_repeat_count = (current_repeat_count * 10) + int(char)

            elif char.isalpha():
                current_pattern += char

            elif char == "[":
                repeat_counts_stack.append(current_repeat_count)
                current_repeat_count = 0

                patterns_stack.append(current_pattern)
                current_pattern = ""

            else:  # char is "]"
                current_pattern = patterns_stack.pop() + (current_pattern * repeat_counts_stack.pop()) 
                
        print(repeat_counts_stack, patterns_stack, current_pattern)

        return current_pattern
