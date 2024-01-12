class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        window = 0
        r_sum = 0
        left = 0
        for right in range(len(costs)):
          r_sum += costs[right]
          while r_sum > coins:
            r_sum -= costs[left]
            left += 1
          if r_sum <= coins:
            window = max(window,right-left+1)
        return window