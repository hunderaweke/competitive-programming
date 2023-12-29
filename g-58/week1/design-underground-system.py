class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id -> (startStaition,time)
        self.totalMap = {} # (start,end) -> [totaltime,count]

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id] = (startStation,t)

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        start,startTime = self.checkInMap[id]
        route = (start,endStation)
        if route not in self.totalMap:
            self.totalMap[route] = [0,0]
        self.totalMap[route][0] += endTime - startTime
        self.totalMap[route][1] += 1        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime,count = self.totalMap[(startStation,endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)