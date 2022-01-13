class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) == 0 or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)