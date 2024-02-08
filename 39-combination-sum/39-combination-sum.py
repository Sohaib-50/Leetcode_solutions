class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def f(current_index, current_sum, current_combo):

            if current_sum == target:
                answer.append(current_combo)
                return 

            if current_sum > target:
                return 

            for idx in range(current_index, len(candidates)):
                current_candidate = candidates[idx]
                current_sum += current_candidate
                f(idx, current_sum, current_combo[:] + [current_candidate])
                current_sum -= current_candidate

        f(0, 0, [])

        return answer
