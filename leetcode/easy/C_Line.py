t = int(input())
for i in range(t):
    n = int(input())
    line = input()
    diffs = [0] * n
    sum = 0
    for l in range(n):
        cur = l if line[l] == "L" else n - l - 1
        mx = l if l > n - l - 1 else n - l - 1
        sum += cur
        diff = mx - cur
        diffs[l] = diff
    diffs.sort(reverse=True)
    for l in range(n):
        sum += diffs[l]
        print(sum, end=" ")
    print()
