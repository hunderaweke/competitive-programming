class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
                continue
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)