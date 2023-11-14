class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            if nums1[-1] ==0:
                nums1.pop()
            else:
                break
        ptr1,ptr2 = 0,0
        while ptr1<len(nums1) and ptr2< len(nums2):
            if nums2[ptr2] <= nums1[ptr1]:
                nums1.insert(ptr1,nums2[ptr2])
                ptr2+=1
            else:
                ptr1+=1
        nums1.extend(nums2[ptr2:])
