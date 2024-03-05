class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def func(ind, first, second):
            if ind >= len(num):
                return True

            target = first + second
            if len(num) - ind < len(str(target)):
                return False

            if int(num[ind : ind + len(str(target))]) == target:
                return func(ind + len(str(target)), second, target)

            return False

        for i in range(1, len(num)-1):
            if i > 1 and num[0] == "0":
                continue

            for j in range(i + 1, len(num)):
                if j > i + 1 and num[i] == "0":
                    continue

                if func(j, int(num[:i]), int(num[i:j])):
                    return True
        return False
