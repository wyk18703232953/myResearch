import random

def main(n: int) -> None:
    # 根据规模 n 生成测试数据：n 个 1~10^9 之间的随机整数
    a = [random.randint(1, 10**9) for _ in range(n)]

    a = sorted(a)
    ans = 0
    b = [0] * n
    for i in range(n):
        if b[i] == 0:
            ans += 1
            for j in range(i, n):
                if a[j] % a[i] == 0:
                    b[j] = 1
    print(ans)


if __name__ == "__main__":
    # 示例：可在此处修改 n 来测试
    main(10)