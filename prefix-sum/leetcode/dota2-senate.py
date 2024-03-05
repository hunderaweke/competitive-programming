class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()
        dires_count = senate.count("D")
        radiants_count = senate.count("R")
        n = len(senate)

        for i, ch in enumerate(senate):
            if ch == "R":
                radiants.append(i)
            else:
                dires.append(i)
        while radiants_count and dires_count:
            if radiants[0] < dires[0]:
                rad = radiants.popleft()
                radiants.append(rad+n)
                dires.popleft()
                dires_count -= 1
            else:
                dire = dires.popleft()
                dires.append(dire+n)
                radiants.popleft()
                radiants_count -= 1
        return "Radiant" if radiants_count else "Dire"