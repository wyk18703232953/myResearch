import random

def main(n: int) -> None:
    a = n  # 规模参数

    # 生成测试数据：4 个 a×a 的 01 矩阵（按原程序是按行拼成一行输入）
    matrices = []
    for _ in range(4):
        # 随机生成 a 行，每行 a 个字符 '0' 或 '1'
        rows = []
        for _ in range(a):
            row = ''.join(random.choice('01') for _ in range(a))
            rows.append(row)
        # 原程序将 a 行拼接成一行字符串
        matrices.append(''.join(rows))

    l = matrices
    total = 0

    # 按原排序逻辑：
    # key = 偶数位中 '1' 的个数 + 奇数位中 '0' 的个数，降序
    l = sorted(
        l,
        key=lambda s: s[0::2].count('1') + s[1::2].count('0'),
        reverse=True
    )

    # 计算 total（严格保持原程序逻辑）
    for z, v in enumerate(l):
        if z < 2:
            # 前两个
            for i in range(a * a):
                if i % 2:
                    total += v[i] != '0'
                else:
                    total += v[i] != '1'
        else:
            # 后两个
            for i in range(a * a):
                if i % 2:
                    total += v[i] != '1'
                else:
                    total += v[i] != '0'

    print(total)


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)