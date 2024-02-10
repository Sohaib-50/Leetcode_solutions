class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        end = len(needle) - 1
        start = 0

        while (end < len(haystack)):

            if (haystack[start] == needle[0]) and (haystack[end] == needle[-1]):
                haystack_left = start
                haystack_right = end
                needle_left = 0
                needle_right = len(needle) - 1

                while (haystack_left <= haystack_right) and (haystack[haystack_left] == needle[needle_left]) and (haystack[haystack_right] == needle[needle_right]):
                    haystack_left += 1
                    needle_left += 1
                    haystack_right -= 1
                    needle_right -= 1
                
                if haystack_left > haystack_right:
                    return start

            end += 1
            start += 1

        return -1
