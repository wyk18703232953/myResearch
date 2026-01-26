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
    if n <= 0:
        return
    # 规模解释：
    # n = 数组长度
    # k = 不同数字的目标个数（确定性地设为 min(5, n)）
    k = 5 if n >= 5 else n
    # 生成确定性数组：包含重复模式，元素范围控制在 [1, 100000] 内
    # arr[i] = (i % max(1, k)) + 1 保证最多 k 种不同元素
    arr = [(i % max(1, k)) + 1 for i in range(n)]
    find_segment(arr, n, k)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值做规模实验
    main(10)