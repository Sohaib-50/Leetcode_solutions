class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index_char_map = {}
        for i in range(len(indices)):
            index_char_map[indices[i]] = s[i]
            
        ans = ["" for i in s]
        for index in index_char_map:
            ans[index] = index_char_map[index]
            
        return "".join(ans)