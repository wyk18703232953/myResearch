import random

def main(n):
    # 生成测试数据：长度为 n 的正整数数组 a，元素范围 1..n
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
                elif any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1

    print(''.join(s))


if __name__ == "__main__":
    # 示例：调用 main(10)，根据需要修改 n
    main(10)