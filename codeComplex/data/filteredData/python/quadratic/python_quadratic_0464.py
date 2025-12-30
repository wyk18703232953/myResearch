import random

def main(n):
    # 生成测试数据：长度为 n 的正整数数组 a
    # 这里生成 1~n 之间的随机数，可按需要自行修改生成规则
    random.seed(0)
    a = [random.randint(1, n) for _ in range(n)]

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
    # 示例：调用 main(10)
    main(10)