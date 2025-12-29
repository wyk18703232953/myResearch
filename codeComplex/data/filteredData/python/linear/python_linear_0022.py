import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 b
    # 为了保证逻辑有意义，至少保证“奇偶性”中存在一个“异类”
    # 先随机选择主奇偶性（0 表示偶数为主，1 表示奇数为主）
    main_parity = random.randint(0, 1)

    # 先生成全部为主奇偶性的数组
    b = []
    for _ in range(n):
        x = random.randint(1, 100)
        if x % 2 != main_parity:
            x += 1  # 调整为主奇偶性
        b.append(x)

    # 随机选择一个位置作为“异类”
    idx = random.randrange(n)
    # 将该位置改为相反奇偶性
    if b[idx] % 2 == 0:
        # 变为奇数
        b[idx] = b[idx] + 1 if b[idx] < 100 else b[idx] - 1
    else:
        # 变为偶数
        b[idx] = b[idx] + 1 if b[idx] < 100 else b[idx] - 1

    # 原始逻辑
    c = [int(i % 2 == 0) for i in b]
    if c.count(1) == 1:
        print(c.index(1) + 1)
    else:
        print(c.index(0) + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)