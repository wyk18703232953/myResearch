import random

def main(n: int):
    # 根据 n 生成测试数据，这里生成 m，保证 m >= 1
    # 原题逻辑对 m 实际没有约束使用，这里随便生成一个与 n 同数量级的 m
    m = random.randint(1, max(1, 10 * n))

    # 原逻辑：读入 n, m 后输出两行
    # 第一行：(n-1) 个字符 '4' 后接一个 '5'
    if n <= 0:
        return  # 规模为非正时，无输出
    print('4' * (n - 1) + '5')

    # 第二行：n 个字符 '5'
    print('5' * n)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)