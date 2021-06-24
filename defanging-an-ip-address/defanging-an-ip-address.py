class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = []
        for char in address:
            if char == ".":
                ans.append("[.]")
            else:
                ans.append(char)
                
        return "".join(ans)