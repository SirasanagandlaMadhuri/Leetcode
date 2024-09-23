ASTEROID COLLISION USING STACKS
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and i<0<stack[-1]:
                if abs(i)>stack[-1]:
                    stack.pop()
                    continue
                if abs(i)==stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(i)           
        return stack
