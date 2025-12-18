def main():
    n, m = list(map(int, input().split()))
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b.sort()
    g.sort()
    if b[-1] > g[0]:
        print(-1)
        return
    if b[-1] == g[0]:
        print(sum(g) + m * (sum(b) - b[-1]))
        return
    if n == 1:
        print(-1)
        return
    print(sum(g) + b[-1] + b[-2] * (m - 1) + m * (sum(b) - b[-1] - b[-2]))
main()