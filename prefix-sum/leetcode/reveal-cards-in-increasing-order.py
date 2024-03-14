class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        order = []
        queue = deque([i for i in range(n)])
        while queue:
            order.append(queue.popleft())
            if queue:
                queue.append(queue.popleft())
        
        ans = [0]*n
        for i in range(n):
            ans[order[i]] = deck[i]
        return ans