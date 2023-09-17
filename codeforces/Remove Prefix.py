n = int(input())
for _ in range(n):
    m = int(input())
    ls = [int(_) for _ in input().split()]
    stack = []
    for j in ls[::-1]:
        if not j in stack:
            stack.append(j)
        else:
            break
    print(m - len(stack))
