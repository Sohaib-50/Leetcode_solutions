class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        while i < len(haystack):

            if haystack[i] != needle[0]:
                i += 1
                continue

            j = i
            k = 0
            while k < len(needle) and j < len(haystack) and needle[k] == haystack[j]:
                j += 1
                k += 1

            if k == len(needle):
                return i

            i += 1

        return -1
