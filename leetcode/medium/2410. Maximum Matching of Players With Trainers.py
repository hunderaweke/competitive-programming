class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pointer1,pointer2 = len(players)-1,len(trainers)-1
        count = 0
        while pointer1>=0 and pointer2>=0:
            if players[pointer1]<= trainers[pointer2]:
                count += 1
                pointer1 -=1
                pointer2 -=1
            elif players[pointer1]> trainers[pointer2]:
                pointer1-=1
        return count
