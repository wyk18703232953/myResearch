import random

MOD = 10**9 + 7

def main(n):
    # 生成测试数据：t 组测试，每组规模为 n
    # 这里设定 t = 1，可按需调整
    t = 1

    for _ in range(t):
        # 生成长度为 n 的数组 a，元素为 1 到 10^9 的随机整数
        a = [random.randint(1, 10**9) for _ in range(n)]
        a.sort()
        if n == 2:
            print(0)
        else:
            print(min(n - 2, a[-2] - 1))


if __name__ == "__main__":
    # 示例：运行规模 n = 5
    main(5)