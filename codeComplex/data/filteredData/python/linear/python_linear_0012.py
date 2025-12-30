def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    j = 3
    while j * j <= n:
        if n % j == 0:
            return False
        j += 2
    return True


# 预先生成参考素数表 ref（与原代码逻辑一致）
ref = [2]
for j in range(3, 1000, 2):
    if prime(j):
        ref.append(j)


def check(n):
    for j in range(1, len(ref) - 1):
        v = n - ref[j] - 1
        if ref[j - 1] == v or ref[j + 1] == v:
            return True
        if j > n:
            break
    return False


# 预先生成 arr（满足 prime 且 check 为 True 的奇数）
arr = []
for j in range(3, 1001, 2):
    if prime(j) and check(j):
        arr.append(j)


def main(n):
    """
    参数 n 用作原始程序中的 n，k 由 n 自动生成：
    这里示例：k = n // 10 + 1（可按需要调整测试策略）
    """
    # 根据规模 n 生成一个测试用 k
    k = max(1, n // 10 + 1)

    count = 0
    for j in range(2, n + 1):
        if j in arr:
            count += 1

    if count >= k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(100)