import random

def main(n: int):
    # 随机生成 U 和数组 E，保证 E 为递增序列
    # 可根据需要调整数据范围
    U = random.randint(1, 10**9)
    E = sorted(random.sample(range(1, 10**9), n))

    mmax = -1.0
    for i in range(0, n - 2):
        j = i + 1
        l = j + 1
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if E[mid] - E[i] <= U:
                l = mid + 1
            else:
                r = mid - 1
        # 修正 l，确保在 [j+1, n-1] 范围内
        if l >= n:
            l = n - 1
        if l <= j:
            continue
        if E[l] - E[i] <= U:
            cur = (E[l] - E[j]) / (E[l] - E[i])
            mmax = max(mmax, cur)
        else:
            if l - 1 > j and E[l - 1] - E[i] <= U:
                cur = (E[l - 1] - E[j]) / (E[l - 1] - E[i])
                mmax = max(mmax, cur)

    print(mmax)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)