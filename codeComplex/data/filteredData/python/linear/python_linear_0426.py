import random

def main(n):
    # 生成测试数据：n 行，每行长度随机，并生成对应的行和
    rows = []
    target_sum = None
    for i in range(n):
        # 每行长度在 1~10 之间
        length = random.randint(1, 10)
        row = [random.randint(-100, 100) for _ in range(length)]
        row_sum = sum(row)
        if i == 0:
            target_sum = row_sum
        rows.append(row_sum)

    # 模拟原逻辑
    a = rows[:]  # 行和列表
    t = target_sum  # 第一行的行和

    a.sort(reverse=True)
    result = a.index(t) + 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)