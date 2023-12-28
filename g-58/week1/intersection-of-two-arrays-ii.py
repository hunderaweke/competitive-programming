class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        c1, c2 = 0, 0
        while c1 < len(nums1) and c2 < len(nums2):
            if nums1[c1] == nums2[c2]:
                res.append(nums1[c1])
                c1 += 1
                c2 += 1
            elif nums1[c1] < nums2[c2]:
                c1 += 1
            else:
                c2 += 1
        return res

