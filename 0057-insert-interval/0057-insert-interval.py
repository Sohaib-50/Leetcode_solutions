class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        current_ptr = 0
        
        # find start interval
        while current_ptr < len(intervals):
            current_interval = intervals[current_ptr]
            if current_interval[1] >= newInterval[0]:
                break
            current_ptr += 1
        start_ptr = current_ptr
        if start_ptr == len(intervals):
            return intervals + [newInterval]
        
        # find end interval
        while current_ptr < len(intervals):
            current_interval = intervals[current_ptr]
            if current_interval[0] > newInterval[1]:
                break
            current_ptr += 1
        end_ptr = current_ptr
        
        print(start_ptr, end_ptr)
        if start_ptr == end_ptr:
            return intervals[:start_ptr] + [newInterval] + intervals[end_ptr:]
                
        return intervals[:start_ptr] + [[min(newInterval[0], intervals[start_ptr][0]), max(newInterval[1], intervals[end_ptr-1][1])]] + intervals[end_ptr:]
        # intervals[start_ptr : end_ptr] = [
        #     [
        #         min(newInterval[0], intervals[start_ptr][0]),
        #         max(newInterval[1], intervals[end_ptr - 1][1])
        #     ]
        # ]
        return intervals
        
        
        
            