class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0,len(letters)-1
        char = letters[-1]

        while left <=  right:
            mid = (left+right)//2
            if letters[mid] > target:
                char = letters[mid] 

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return char if char > target else letters[0]