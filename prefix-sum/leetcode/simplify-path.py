class Solution:
    def simplifyPath(self, path: str) -> str:
        simPath = path.split('/')
        stack = []
        for i in simPath:
            if i=="." or i == "":
                pass
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+'/'.join(stack)
