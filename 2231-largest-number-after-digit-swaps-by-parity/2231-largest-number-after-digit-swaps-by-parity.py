class Solution:
    def largestInteger(self, num: int) -> int:
        frequency = [0 for i in range(10)]
        even_idx = 0
        odd_idx = 1
        answer = 0
        
        i = 0
        while (num // (10 ** i) != 0):
            frequency[(num // (10 ** i)) % 10] += 1
            i += 1
            
        i = 0
        while (num // (10 ** i) != 0):
            current_digit = (num // (10 ** i)) % 10

            # if current digit in num is even, find largest current even number
            if current_digit % 2 == 0:
                while frequency[even_idx] == 0:
                    even_idx += 2
                answer += even_idx * (10 ** i)
                frequency[even_idx] -= 1

            else:
                while frequency[odd_idx] == 0:
                    odd_idx += 2
                answer += odd_idx * (10 ** i)
                frequency[odd_idx] -= 1
            
            i += 1

        return answer
                
                
            