import random

def main(n: int):
    # 生成规模为 n 的测试数据：n 个 1~n 之间的整数
    A = sorted(random.randint(1, max(1, n)) for _ in range(n))

    B = [0] * 100
    for i in A:
        j = 0
        # 找到第一个为 0 的位置
        for c in range(100):
            if B[c] == 0:
                j = c
                break

        # 从 j 开始，每隔 i 位置标记为 1
        while j < 100:
            B[j] = 1
            j += i

    if B.count(0) == 0:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)