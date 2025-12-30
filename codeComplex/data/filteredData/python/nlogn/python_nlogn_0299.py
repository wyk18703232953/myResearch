import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个座位的重要程度（原代码是读一行数字）
    # 这里用 1~100 的随机整数
    seat_values = [random.randint(1, 100) for _ in range(n)]
    # 生成一个长度为 n 的字符串，只含 '0' 或 '1'
    # 保证至少有一个 '0'，避免一开始 one_seat 为空而 pop 报错
    persons = ['0']
    persons += [random.choice(['0', '1']) for _ in range(n - 1)]
    persons = ''.join(persons)

    # 2. 原逻辑：处理 two_seats 和 one_seat
    one_seat = []
    two_seats = []
    j = 1

    # 将生成的 seat_values 转成 (value, index) 列表
    for item in seat_values:
        two_seats.append((int(item), j))
        j += 1

    # 按 value 从大到小排序
    two_seats.sort(key=lambda x: -x[0])

    # 模拟原程序的输出逻辑
    output_indices = []
    for person in persons:
        if person == '0':
            q = two_seats.pop()
            output_indices.append(str(q[1]))
            one_seat.append(q)
        else:
            output_indices.append(str(one_seat.pop()[1]))

    # 输出结果
    print(' '.join(output_indices))


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)