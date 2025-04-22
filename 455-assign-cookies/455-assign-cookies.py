class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_idx = 0
        cookie_idx = 0
        content = 0
        while (cookie_idx < len(s)) and (child_idx < len(g)):
            if s[cookie_idx] >= g[child_idx]:
                content += 1
                child_idx += 1
            cookie_idx += 1
        
        return content
