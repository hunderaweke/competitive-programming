class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join([i.lower() for i in s if i.isalnum()])
        return newS==newS[::-1]