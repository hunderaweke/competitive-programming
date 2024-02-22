class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i ==  '{' or i == '(' or i=='[':
                stack.append(i)
            elif stack and i == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and i == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        return False if stack else True