import math

n = int(input())
for i in range(n):
    m = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    ls[0] += 1
    print(math.prod(ls))
