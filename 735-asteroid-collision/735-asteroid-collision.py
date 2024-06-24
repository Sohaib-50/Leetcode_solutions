class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            asteroid = asteroids[i]

            while stack and (asteroid < 0 and stack[-1] > 0):
                if abs(stack[-1]) > abs(asteroid):
                    asteroid = 0
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    asteroid = 0


            if asteroid != 0:
                stack.append(asteroid)

        return stack
