class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_white = 0
        recolor = k
        left = 0
        for right in range(len(blocks)):
            count_white +=  blocks[right] == "W"
            if right - left+1 >k:
                count_white -= blocks[left] == "W"
                left += 1
            if right-left+1 == k:
                recolor = min(recolor,count_white)
        return recolor