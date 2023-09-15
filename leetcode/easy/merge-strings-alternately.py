class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = [_ for _ in word1[::-1]]
        word2 = [_ for _ in word2[::-1]]
        ls = ["" for _ in range(len(word1) + len(word2))]
        for i in range(len(ls)):
            if not word1 or not word2:
                ls[i] += word1.pop() if not word2 else word2.pop()
            elif not i % 2:
                ls[i] = word1.pop()
            else:
                ls[i] = word2.pop()
        return "".join(ls)