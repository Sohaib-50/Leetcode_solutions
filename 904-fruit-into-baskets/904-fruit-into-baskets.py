class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        collected_fruits = set()
        max_fruits = float('-inf')

        win_start = 0
        for win_end, fruit in enumerate(fruits):
            
            # max_fruits = max(max_fruits, win_end - win_start + 1)

            if len(collected_fruits) < 2:
                collected_fruits.add(fruit)                

            elif fruit not in collected_fruits:
                win_start = win_end - 1
                while (fruits[win_start - 1] == fruits[win_end - 1]): 
                    win_start -= 1
                # print(f"{win_end, fruit}, Adjusted win_start to {win_start}")
                collected_fruits.add(fruit)
                collected_fruits.remove(fruits[win_start - 1])
            
            max_fruits = max(max_fruits, win_end - win_start + 1)
            # print(f"{win_end, fruit} win_size {win_end - win_start + 1}")

                

        return max_fruits



            
