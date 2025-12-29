import random


def main(n: int):
    # 1. 生成规模为 n 的测试数据：1..n 的随机排列
    perm = list(range(1, n + 1))
    random.shuffle(perm)

    # 模拟原程序读取后的数据结构
    positions = {}
    pos2x = {}
    for i, x in enumerate(perm):
        positions[x] = i
        pos2x[i] = x

    answers = ['' for _ in range(len(positions))]

    for x in range(len(positions), 0, -1):
        position = positions[x]

        def can_go_to_looser():
            # 向右跳
            next_position = position + x
            while next_position < len(positions):
                if pos2x[next_position] > x and answers[next_position] == "B":
                    return True
                next_position += x

            # 向左跳
            next_position = position - x
            while next_position >= 0:
                if pos2x[next_position] > x and answers[next_position] == "B":
                    return True
                next_position -= x

            return False

        if can_go_to_looser():
            answers[position] = "A"
        else:
            answers[position] = "B"

    # 输出结果
    print(''.join(answers))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)