n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
numsSmaller = 0
ptr1, ptr2 = 0, 0

while ptr1 < n and ptr2 < m:
    while ptr1 < n and ptr2 < m and arr1[ptr1] < arr2[ptr2]:
        numsSmaller += 1
        ptr1 += 1
    else:
        ptr2 += 1
    res.append(numsSmaller)

while ptr2 < m:
    ptr2 += 1
    res.append(numsSmaller)

print(*res)
