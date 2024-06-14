class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # count occurance of each number in arr
        frequency_map = {}
        for num in arr:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # find if any occurance count repeats
        occurrences = set()
        for num in frequency_map:
            occurrence = frequency_map[num]
            if occurrence in occurrences:
                return False
            occurrences.add(occurrence)

        return True
