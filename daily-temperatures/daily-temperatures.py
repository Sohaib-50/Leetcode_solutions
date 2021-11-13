class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in temperatures]
        monotonic_stack = []
        for i in range(len(temperatures)):
            while (len(monotonic_stack) != 0) and (temperatures[i] > temperatures[monotonic_stack[-1]]):
                ans[monotonic_stack[-1]] = i - monotonic_stack[-1]
                monotonic_stack.pop()
            monotonic_stack.append(i)
            
        return ans
                