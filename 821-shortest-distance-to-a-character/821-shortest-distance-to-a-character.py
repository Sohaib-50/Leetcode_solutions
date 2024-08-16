class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        ans = [float('inf') for _ in s]

        # find shortest distances acc to right movemement
        closest_pos = float('inf')
        for i in range(len(s)):
            ch = s[i]
            if ch == c:
                closest_pos = i
            ans[i] = abs(closest_pos - i)
        
        # find shortest distances acc to left movemement
        closest_pos = float('inf')
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == c:
                closest_pos = i
            ans[i] = min(ans[i], abs(closest_pos - i))

        return ans
