class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        answer = []
        while i < len(command):
            current_char = command[i]
            if current_char == "G":
                answer.append("G")
                i += 1
            else:
                if command[i + 1] == ")":
                    answer.append("o")
                    i += 2
                else:
                    answer.append("al")
                    i += 4
                    
        return "".join(answer)
