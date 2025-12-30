import random

def main(n):
    # 生成测试数据：m 为随机的标记个数，这里设为 [n, 2n] 范围
    m = random.randint(n, 2 * n)

    # 随机生成 m 个在 [1, n] 之间的整数，模拟原来的输入 c
    c = [str(random.randint(1, n)) for _ in range(m)]

    # 以下为原始逻辑的封装
    col = [0] * n
    for value in c:
        col[int(value) - 1] += 1

    print(min(col))


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时按需修改 n
    main(5)