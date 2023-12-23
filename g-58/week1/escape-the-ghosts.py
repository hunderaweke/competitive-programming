class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        hset  = set()
        for ghost in ghosts:
            x = abs(ghost[0]-target[0])
            y = abs(ghost[1]-target[1])
            hset.add(x+y)
        dist = abs(target[0]) + abs(target[1])
        if dist < min(hset):
            return True
        return False