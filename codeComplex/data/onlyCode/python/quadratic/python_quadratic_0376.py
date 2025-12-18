n, m = list(map(int, input().split()))
temp = 0
a = [list(input()) for i in range(n)]
for i in range(n):
    ok = False
    for j in range(m):
        if (a[i][j] == "B"):
            pos1 = i
            pos2 = j
            temp += 1
            temp2 = j
            if (j != m-1):
                ok = True
                while True:
                    ok2 = False
                    if (temp2 == m-1):
                        ok2 = True
                        break
                    if (a[i][temp2 + 1] != "B"):
                        ok2 = True
                        break
                    temp += 1
                    temp2 += 1
            elif (j == m - 1):
                temp = 1
                ok = True
                break
            if (ok2):
                break
    if (ok):
        break
print(temp//2 + pos1 + 1, temp//2 + pos2 + 1)