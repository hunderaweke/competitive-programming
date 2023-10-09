#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        c1, c2 = 0, 0
        while c1 < len(nums1) and c2 < len(nums2):
            if nums1[c1] == nums2[c2] and nums1[c1] not in res:
                res.append(nums1[c1])
                c1 += 1
                c2 += 1
            elif nums1[c1] > nums2[c2]:
                c2 += 1
            else:
                c1 += 1
        return res


# @lc code=end
