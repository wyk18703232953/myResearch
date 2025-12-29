import random

def main(n):
    # 生成测试数据
    # K 在 [0, n] 范围内随机
    K = random.randint(0, n)
    # 生成 n 个随机整数，范围可自行调整
    b = [random.randint(0, 10 * n) for _ in range(n)]

    # 原逻辑
    b = sorted(b)
    l = cur = 0
    for i in range(1, n):
        if b[i] == b[i - 1]:
            continue
        if b[i] > b[i - 1] + K:
            l = i
        else:
            cur += (i - l)
            l = i
    print(n - cur)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)