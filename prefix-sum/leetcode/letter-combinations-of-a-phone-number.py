class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combination = []
        hash_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def dfs(ind,curr):
            if len(curr) == len(digits):
                combination.append("".join(curr))
                return
            chars = hash_map[digits[ind]]
            for i in range(len(chars)):
                curr.append(chars[i])
                dfs(ind+1,curr)
                curr.pop()
        dfs(0,[])
        return combination

