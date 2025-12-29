import random

def main(n):
    # 生成规模为 n 的测试数据
    # 约定：m <= n，a 和 c 中元素为 1~10^9 的随机整数
    m = random.randint(0, n)  # m 在 [0, n] 范围内
    c = [random.randint(1, 10**9) for _ in range(n)]
    a = [random.randint(1, 10**9) for _ in range(m)]

    # 保持与原逻辑一致
    j, res = 0, 0
    for i in range(n):
        if j < m:
            if c[i] <= a[j]:
                j += 1
                res += 1

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)