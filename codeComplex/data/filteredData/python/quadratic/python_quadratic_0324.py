import heapq

def main(n):
    # 映射输入规模 n 到原程序的 (n, d, k)
    # 为保证可扩展与确定性，选取：
    #   N = max(2, n)
    #   D = max(1, min(N - 1, n // 2))
    #   K = max(1, min(10, n // 3))
    N = max(2, n)
    D = max(1, min(N - 1, n // 2))
    K = max(1, min(10, n // 3))

    n_val, d, k = N, D, K

    if n_val == 1 or n_val <= d:
        ans = "NO"
        e = []
    elif k == 1:
        ans = "YES" if n_val == 2 and d == 1 else "NO"
        e = [(1, 2)] if ans == "YES" else []
    else:
        e = [(i + 1, i + 2) for i in range(d)]
        h = []
        l, r = 1, d + 1
        if k > 2:
            for i in range(2, d + 1):
                heapq.heappush(h, (i, 2, min(i - l, r - i)))
        ans = "YES"
        for i in range(d + 2, n_val + 1):
            if not h:
                ans = "NO"
                break
            j, k0, d0 = heapq.heappop(h)
            e.append((j, i))
            if k0 + 1 < k:
                heapq.heappush(h, (j, k0 + 1, d0))
            if d0 - 1 > 0:
                heapq.heappush(h, (i, 1, d0 - 1))

    print(ans)
    if ans == "YES":
        for u, v in e:
            print(u, v)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)