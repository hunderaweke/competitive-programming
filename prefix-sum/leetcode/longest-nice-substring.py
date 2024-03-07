class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(string):
            hashset = set(string)
            if not string:
                return ""

            for i in range(len(string)):
                if not (string[i].lower() in hashset and string[i].upper() in hashset):
                    string1 = dfs(string[:i])
                    string2 = dfs(string[i+1:])
                    return string2 if len(string2)>len(string1) else string1
            return string

        return dfs(s)