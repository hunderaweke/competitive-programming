class LargerNumberKey(str):
    def __lt__(x,y):
        return x+y>y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = ''.join(sorted(map(str,nums),key=LargerNumberKey))
        return num if num[0]!= '0' else '0'