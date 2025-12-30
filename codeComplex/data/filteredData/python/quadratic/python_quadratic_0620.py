import random

def main(n: int) -> int:
    # 生成测试数据
    # 约定：1 <= m <= n，k 为适当范围的非负整数，a 为整数数组
    if n <= 0:
        return 0

    m = random.randint(1, n)
    k = random.randint(0, 10)
    a = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑
    ret = 0
    for i in range(m):
        cur = 0
        for j in range(i, n):
            if j % m == i:
                cur = max(0, cur)
                cur -= k
            cur += a[j]
            ret = max(ret, cur)

    return ret


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时由外部决定 n
    print(main(10))