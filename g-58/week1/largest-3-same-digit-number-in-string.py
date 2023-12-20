class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left = 0
        ans  = float("-inf")
        for right in range(len(num)):
            if num[right] != num[left]:
                left  = right
                continue
            if right - left + 1 == 3:
                ans = max(ans,int(num[left:right + 1]))
        if ans == 0:
            return "000"
        return f"{ans}" if ans > float("-inf") else ""