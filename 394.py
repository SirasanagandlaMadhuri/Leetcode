decode string
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]       
        for i in s:
            if i==']':
                ans=""
                while stack and stack[-1]!='[':
                    ans=stack.pop()+ans
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(int(num)*ans)
            else:
                stack.append(i)
        return ''.join(stack)
