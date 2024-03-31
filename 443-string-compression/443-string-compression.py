class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        current_group_len = 0

        while i < len(chars):
            current_group_len += 1

            # end of group
            if (i == len(chars) - 1) or (chars[i] != chars[i + 1]):
        
                # add group character
                chars[j] = chars[i]
                j += 1

                # add group length if greater than 1
                if current_group_len > 1:
                    for num in str(current_group_len):
                        chars[j] = num
                        j += 1
                
                current_group_len = 0

            i += 1

        return j 
            
