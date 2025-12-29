import random

def main(n: int):
    # 1. 生成测试数据 b，长度为 n
    #   这里示例：b 为 1..n 的前缀和，保证非负且递增，便于调试
    b = []
    curr = 0
    for i in range(1, n + 1):
        curr += i
        b.append(curr)

    # 2. 按照原始逻辑计算 a1, a2 并输出
    a1 = [0]
    a2 = [b[0]]

    for x in b[1:]:
        new_a = a1[-1]
        if x - new_a > a2[-1]:
            new_a = x - a2[-1]
        new_a2 = x - new_a
        a1.append(new_a)
        a2.append(new_a2)

    print(*(a1 + a2[::-1]))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)