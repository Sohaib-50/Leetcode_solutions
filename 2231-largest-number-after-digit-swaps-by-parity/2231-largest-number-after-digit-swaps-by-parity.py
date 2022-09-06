class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        
        even_nums = [i for i in nums if i % 2 == 0]
        even_nums.sort()
        
        odd_nums = [i for i in nums if i % 2 != 0]
        odd_nums.sort()
        
        answer = []
        for i in nums:
            if i % 2 == 0:
                answer.append(even_nums.pop())
            else:
                answer.append(odd_nums.pop())
        
        return int("".join([str(c) for c in answer]))