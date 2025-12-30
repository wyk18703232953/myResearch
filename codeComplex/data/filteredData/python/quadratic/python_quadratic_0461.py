import random

def main(n: int) -> str:
    # 生成测试数据：a 为 1..n 范围内的随机整数
    # 可以按需修改生成规则
    a = [random.randint(1, n) for _ in range(n)]

    b = [0] * n  # 保留原代码里未使用的数组，以保持结构
    s = [0] * n
    m = n

    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                # 注意：如果 x 为 0，会导致 range 步长为 0 出错。
                # 这里假设生成的数据中 x >= 1。
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
    result = ''.join(s)
    print(result)
    return result


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改规模
    main(5)