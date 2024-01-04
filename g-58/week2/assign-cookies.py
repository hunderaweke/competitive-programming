class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        children.sort()
        cookies.sort()
        ptr1,ptr2 = 0,0
        count = 0
        # Pushing the place of the ptr1 in the children array will be the number of the childern we can content
        while ptr1 < len(cookies) and ptr2 < len(children):
            if cookies[ptr1] >= children[ptr2]:
                count += 1
                ptr2 += 1
            ptr1 += 1
        return count