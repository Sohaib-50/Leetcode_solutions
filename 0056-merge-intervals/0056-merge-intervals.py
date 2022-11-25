class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]
       
        for i in range(1, len(intervals)):
            if merged_intervals[-1][1] >= intervals[i][0]:
                merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], intervals[i][1])]
            else:
                merged_intervals.append(intervals[i])
                
        return merged_intervals