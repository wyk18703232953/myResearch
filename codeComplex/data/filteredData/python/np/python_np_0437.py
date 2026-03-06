def main(n):
    m = n
    if m <= 0:
        print(1, 1)
        return
    a = [[(i * 131 + j * 17) % int(1e9) for j in range(m)] for i in range(n)]
    ans = []
    le = 0
    ri = int(1e9)

    def check(mid: int) -> bool:
        nonlocal ans
        dic = {}
        for i in range(n):
            bit = 0
            for j in range(m):
                if a[i][j] >= mid:
                    bit += 1
                bit <<= 1
            dic[bit >> 1] = i
        full = (1 << m) - 1
        for x, idx in dic.items():
            for y, idy in dic.items():
                if x | y == full:
                    ans = (idx + 1, idy + 1)
                    return True
        return False

    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri = mid - 1
    if ans:
        print(ans[0], ans[1])
    else:
        print(1, 1)


if __name__ == "__main__":
    main(5)