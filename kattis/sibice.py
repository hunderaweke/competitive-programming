n, w, h = [int(i) for i in input().split()]
d = ((w**2) + (h**2)) ** 0.5
for i in range(n):
    print("DA" if int(input()) <= d else "NE")
