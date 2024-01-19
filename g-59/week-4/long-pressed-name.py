class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1 = 0
        for ptr2 in range(len(typed)):
            if ptr1< len(name) and name[ptr1] == typed[ptr2]:
                ptr1 += 1
            elif ptr2 == 0 or typed[ptr2] != typed[ptr2-1]:
                return False
        return ptr1 == len(name)