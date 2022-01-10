class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        opening_braces = {"(", "[", "{"}
        for char in s:
            if char in opening_braces:
                stack.append(char)
            else:  # char is a closing brace
                if len(stack) == 0:
                    return False
                elif char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:  # char == }
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                    
        return len(stack) == 0
        # curlies = []
        # squares = []
        # rounds = []
        # for char in s:
        #     if char == "(":
        #         rounds.append(char)
        #     elif char == "[":
        #         squares.append(char)
        #     elif char == "{":
        #         curlies.append(char)
        #     elif char == ")":
        #         if len(rounds) != 0:
        #             rounds.pop()
        #         else:
        #             return False
        #     elif char == "]":
        #         if len(squares) != 0:
        #             squares.pop()
        #         else:
        #             return False
        #     else:  # char == "}"
        #         if len(curlies) != 0:
        #             curlies.pop()
        #         else:
        #             return False
        # return True