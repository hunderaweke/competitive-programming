class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counter = defaultdict(int)
        left = 0
        min_distance = math.inf
        for right,card in enumerate(cards):
            counter[card] += 1
            while counter[card] > 1:
                min_distance = min(right-left+1,min_distance)
                counter[cards[left]] -= 1
                left += 1
        return min_distance if min_distance != math.inf else -1