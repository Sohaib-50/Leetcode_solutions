class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [None for _ in range(n)]
        
        for i in range(1, n+1):
            x = ""
            if i % 3 == 0:
                x += "Fizz"
            if i % 5 == 0:
                x += "Buzz"
            
            ans[i - 1] = x if x != "" else str(i)
        
        return ans