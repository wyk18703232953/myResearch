import random

def main(n):
    # 生成测试数据：a 为长度为 n 的正整数数组，元素范围 [1, n]
    a = [random.randint(1, n) for _ in range(n)]

    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            r = range(i % x, n, x)
            if s[i] == 0:
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
    print(''.join(s))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)