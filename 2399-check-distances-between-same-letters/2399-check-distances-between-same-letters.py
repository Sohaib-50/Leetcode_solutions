class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_occurances = [-1 for _ in range(26)]

        for idx, char in enumerate(s):
            char_number = ord(char) - ord('a')
            first_occurance = first_occurances[char_number]

            # if not seen yet
            if first_occurance == -1:
                first_occurances[char_number] = idx

            # if seen earlier, check if distance same as given
            else:
                char_distance = idx - first_occurance - 1
                if char_distance != distance[char_number]:
                    return False
        
        return True
