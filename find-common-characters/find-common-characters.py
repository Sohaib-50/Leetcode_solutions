class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        commons = {}
        for char in A[0]:
            if char in commons:
                commons[char] += 1
            else:
                commons[char] = 1
        
        for string in A:
            current = {char: 0 for char in commons}
            for char in string:
                if char in current:
                    current[char] += 1
            
            for char in commons:
                if (current[char] < commons[char]):
                    commons[char] = current[char]
        
        answer = []
        for char in commons:
            if commons[char] != 0:
                for i in range(commons[char]):
                    answer.append(char)
            
        return answer
    