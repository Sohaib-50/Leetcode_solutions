class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [None for _ in range(n)]
        mappings = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n+1):
            output = ""
            for num in mappings:
                if i % num == 0:
                    output += mappings[num]
            ans[i - 1] = output if (output != "") else str(i)
        
        return ans