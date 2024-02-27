class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        hash_map = {"0":"01","1":"10"}
        def generate(string,n,k):
            if n == 1:
                return string[k-1]
            if k > 2**(n-1):
                k -= 2**(n-1)
                return generate(hash_map[string[1]],n - 1,k)
            return generate(hash_map[string[0]],n - 1,k)
        ans  = generate("01",n,k)
        return int(ans)