import random

def main(n: int) -> None:
    # 生成测试数据：长度为 n 的正整数数组 a
    # 这里生成 1..n 范围内的随机整数，可按需要调整
    random.seed(0)
    a = [random.randint(1, max(1, n)) for _ in range(n)]

    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if s[i] == 0 and any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
    print(''.join(s))


if __name__ == "__main__":
    # 示例调用：n 可按需修改或在外部调用 main(n)
    main(10)