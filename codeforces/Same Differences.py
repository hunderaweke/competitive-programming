n = int(input())
for i in range(n):
    input()
    ls = [int(_) for _ in input().split()]
    r, l, counter = len(ls) - 1, 0, 0
    while r > l:
        print(r, l)
        if l == r:
            break
        elif l + 1 == r:
            l = 0
        elif r - l == ls[r] - ls[l]:
            counter += 1
        elif ls[r] - ls[l] != r - l and l + 1 != r:
            l += 1
        elif ls[r] - ls[l] != r - l:
            r -= 1
    print(counter)
