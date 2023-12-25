class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looses = defaultdict(int)
        for winner,looser in matches:
            if winner not in looses:
                looses[winner] = 0
            looses[looser]+=1
        ans = [[i for i in looses if looses[i]==0],[i for i in looses if looses[i]==1]]
        ans[0].sort()
        ans[1].sort()
        return ans