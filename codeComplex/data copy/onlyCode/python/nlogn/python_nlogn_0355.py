from sys import stdin
input = stdin.readline

def solve():
    n = int(input())
    x = [int(x) for x in input().split()]
    s = set(x)
    ans = [x[0]]
    for i in range(n):
        for j in range(0, 32):
            if x[i] + 2**j in s:
                ans = [x[i], x[i] + 2**j]
                if x[i] + (2**j * 2) in s:
                    ans.append(x[i] + (2**j * 2))
                    return ans
    return ans

ans = solve()
print(len(ans))
print(*ans)