import random

def main(n):
    # 生成测试数据
    # 参数范围可按需调整
    A = random.randint(0, 10)
    B = random.randint(0, 10)
    C = random.randint(0, 10)
    T = random.randint(1, 10)
    a = [random.randint(0, T) for _ in range(n)]

    ans = 0
    for i in range(n):
        su, cur = A, A
        for j in range(a[i], T):
            cur -= B
            su = max(su, (j - a[i] + 1) * C + cur)
        ans += su

    print(ans)


if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(5)