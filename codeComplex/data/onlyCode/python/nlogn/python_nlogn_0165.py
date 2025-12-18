import sys
readline = sys.stdin.readline

def main():
    N = int(input())
    itvs = []
    for _ in range(N):
        x, w = map(int, input().split())
        itvs.append((x - w, x + w))
    itvs.sort(key=lambda x: x[1])

    ans = 0
    end = -(10**9 + 1)
    for l, r in itvs:
        if end <= l:
            ans += 1
            end = r
    print(ans)

if __name__ == "__main__":
    main()

