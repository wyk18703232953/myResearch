import sys


# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline


t = 1

while t:
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    diffs = []
    for i in range(n):
        if a[i] != b[i]:
            diffs.append(i)
    
    if len(diffs) > 2:
        print("NO")
    elif not diffs:
        print("YES")
    else:
        i, j = diffs
        if a[i] == b[j] and b[i] == a[j]:
            print("YES")
        else:
            print("NO")




    