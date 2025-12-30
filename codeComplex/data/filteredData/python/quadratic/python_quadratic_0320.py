import random

def main(n: int):
    # 参数设置
    k = max(1, n // 5)  # 例如取窗口下界为 n/5，至少为1

    # 生成测试数据：长度为 n 的整数数组 a
    # 这里用 -100 到 100 的随机整数
    random.seed(0)
    a = [random.randint(-100, 100) for _ in range(n)]

    # 原逻辑
    r = 0.0
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    for i in range(n - k + 1):
        for j in range(i + k, min(n + 1, i + 2 * k)):
            r = max(r, (s[j] - s[i]) / (j - i))
    print(r)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)