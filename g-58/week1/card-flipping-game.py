class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        store = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in store:
                store.remove(fronts[i])
        if len(store) ==0 :
            return 0
        return store.pop()