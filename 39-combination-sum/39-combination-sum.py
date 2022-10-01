class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solver(target, current_index, current_sequence, output):
            if target == 0:
                output.append(current_sequence)
                return
            elif (target < 0) or (current_index >= len(candidates)):
                return
            
            current_num = candidates[current_index]
            
            # include current index
            solver(target - current_num,
                   current_index,
                   current_sequence + [current_num],
                   output)
            
            # don't include current index
            solver(target,
                   current_index + 1,
                   current_sequence,
                   output)
            
        output = []
        solver(target, 0, [], output)
        return output