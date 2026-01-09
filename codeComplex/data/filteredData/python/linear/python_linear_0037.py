def find_segment(arr, n, k):
    f = [0] * 100001
    L = 0
    count = 0
    R = -1
    while R < n - 1:
        R += 1
        if f[arr[R]] == 0:
            count += 1
        f[arr[R]] += 1
        while count == k:
            f[arr[L]] -= 1
            if f[arr[L]] == 0:
                # print(L + 1, R + 1)
                pass
                return
            L += 1
    # print(-1, -1)
    pass


def main(n):
    # 定义 k 为规模的一部分，这里设为 min(n, 20)
    k = min(n, 20)
    if n == 0:
        # print(-1, -1)
        pass
        return
    # 构造一个确定性的数组，元素值控制在 1..100000 以内
    # 使用简单的线性同余形式保证分布均匀且确定
    arr = [((i * 37 + 11) % 100000) + 1 for i in range(n)]
    find_segment(arr, n, k)


if __name__ == "__main__":
    main(1000)