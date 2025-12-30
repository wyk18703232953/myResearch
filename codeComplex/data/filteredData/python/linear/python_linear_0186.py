import random

def main(n: int):
    # 生成规模为 n 的测试数据：n 个 1 到 10 之间的随机整数
    number_sequence = [random.randint(1, 10) for _ in range(n)]

    number_total = sum(number_sequence)

    current_total = 0
    current_position = 0

    for number in number_sequence:
        current_total += number
        current_position += 1
        if current_total >= number_total / 2:
            print(current_position)
            break


if __name__ == "__main__":
    # 示例：可自行修改测试规模
    main(10)