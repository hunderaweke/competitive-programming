class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        guardSet = set((tuple(guard) for guard in guards))
        wallsSet = set((tuple(wall) for wall in walls))
        guarded = set()
        for gx, gy in guards:
            for dx, dy in dirs:
                x = gx
                y = gy
                while (
                    (0 <= dx + x < m)
                    and (0 <= dy + y < n)
                    and (tuple([x + dx, y + dy]) not in wallsSet)
                    and (tuple([x + dx, y + dy]) not in guardSet)
                ):
                    guarded.add((x + dx, y + dy))
                    x += dx
                    y += dy
        return (m * n) - len(guarded) - len(guardSet) - len(wallsSet)