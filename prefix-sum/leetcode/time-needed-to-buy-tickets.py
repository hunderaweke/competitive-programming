class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque([[j,i] for i,j in enumerate(tickets)])
        d = {i:j for i,j in enumerate(tickets)}
        while True:
          t = queue.popleft()
          if d[k] == 0:
            break
          if t[0]:
            t[0] -= 1
            d[t[1]] -= 1
            queue.append(t)
            count += 1
          else:
            queue.append(t)
        return count
