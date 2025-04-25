class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurances = {}
        for i, char in enumerate(s):
            last_occurances[char] = i
        
        ans = []
        partition_start = 0
        partition_end = last_occurances[s[0]]

        for i, char in enumerate(s):
            partition_end = max(partition_end, last_occurances[char])

            if i == partition_end:
                ans.append(partition_end - partition_start + 1)
                partition_start = i + 1
                
        return ans
