class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            if not stack:
                stack.append((idx,temp))
            if stack:
                while stack and stack[-1][1] < temp:
                    popped = stack.pop()
                    res[popped[0]] = idx-popped[0]
                stack.append((idx,temp))
        return res
