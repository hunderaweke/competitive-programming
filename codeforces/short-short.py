n = int(input())
for i in range(n):
    k = input()
    if k[0] == "a" and k[-1] == "c":
        print("YES")
    elif k[1] == "c" and k[-1] == "b":
        print("YES")
    elif k[0] == "c" and k[-1] == "a":
        print("YES")
    elif k[1] == "a" and k[0] == "b":
        print("YES")
    else:
        print("NO")
