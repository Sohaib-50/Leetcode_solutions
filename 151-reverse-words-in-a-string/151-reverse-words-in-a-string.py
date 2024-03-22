class Solution:
    def reverseWords(self, s: str) -> str:
        '''Aproach 2'''
        ans = ""
        current_word = ""
        for i in range(len(s)):
            current_char = s[i]

            # add to current word if char is non space
            if current_char != " ":
                current_word = current_word + current_char

            # add currently formed word to ans if space or end of input and word present
            if (current_char == " " or i == len(s) - 1) and current_word != "":
                ans = current_word + " " + ans  # add word to start of ans (to keep reverse order)
                current_word = ""  # reset current word to start recording next one

        return ans.strip()



    # def reverseWords(self, s: str) -> str:
    #     '''Aproach 1'''
    #     words = []
    #     current_word = ""
    #     for char in s:
    #         if char == " " and current_word != "":
    #             words.append(current_word)
    #             current_word = ""
    #         elif char != " ":
    #             current_word += char
    #     if current_word != "":
    #         words.append(current_word)
    #     ans = ""
    #     for i in range(len(words) - 1, -1, -1):
    #         ans += words[i] + (" " if i != 0 else "")
    #     return ans
                    

    # def reverseWords(self, s: str) -> str:
    #     '''Aproach 0'''
    #     s = s.strip()
    #     s = s.split(" ")
    #     s = list(filter(lambda x: x != "", s))
    #     s = " ".join(reversed(s))
    #     return  s
