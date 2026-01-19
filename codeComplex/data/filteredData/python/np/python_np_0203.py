import sys

INF = 10**20
MOD = 10**9 + 7

def main(n):
    # 映射规则：
    # n: 元素个数
    # a[i] = i+1
    # l = n
    # r = n * (n + 1) // 2
    # x = max(1, n // 4)
    if n <= 0:
        print(0)
        return

    a = [i + 1 for i in range(n)]
    l = n
    r = n * (n + 1) // 2
    x = max(1, n // 4)

    ans = 0
    for mask in range(1, 1 << n):
        if mask & (mask - 1) == 0:
            continue
        mn, mx, total = INF, -INF, 0
        j = 0
        while j < n:
            if (mask >> j) & 1:
                val = a[j]
                if val < mn:
                    mn = val
                if val > mx:
                    mx = val
                total += val
            j += 1
        if l <= total <= r and mx - mn >= x:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main(10)