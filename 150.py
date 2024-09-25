EVALUATE REVERSE POLISH NOTATION
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                b=int(stack.pop())
                c=int(stack.pop())
                if i=="+":    
                        stack.append(c+b)
                elif i=="*":
                        stack.append(c*b)
                elif i=="/":
                        stack.append(int(c/b))
                elif i=="-":
                        stack.append(c-b)
        return stack[0]
