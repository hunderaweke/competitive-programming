class Robot:

    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.perimeter = 2*(width+height-2)
        self.atStart = True
        self.pos = 0
        self.bottomRight = width-1
        self.topRight = self.bottomRight + (height-1)
        self.topLeft = self.topRight + (width-1)

    def step(self, num: int) -> None:
        self.atStart = False
        self.pos = (self.pos+num) % self.perimeter

    def getPos(self) -> List[int]:
        if 0 <= self.pos <= self.bottomRight:
          return [self.pos,0]
        if self.bottomRight < self.pos <= self.topRight:
          return [self.width-1,self.pos-self.bottomRight]
        if self.topRight < self.pos <= self.topLeft:
          return[self.bottomRight-(self.pos-self.topRight),self.height - 1]
        return [0,self.topRight-self.bottomRight - (self.pos-self.topLeft)]
    def getDir(self) -> str:
        if self.atStart or 0 < self.pos <= self.bottomRight:
          return "East"
        if self.bottomRight < self.pos <= self.topRight:
          return "North"
        if self.topRight < self.pos <= self.topLeft:
          return "West"
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()