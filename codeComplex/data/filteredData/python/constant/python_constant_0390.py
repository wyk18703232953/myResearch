import random

def main(n: int):
    # 生成两行长度为 n 的测试数据，只包含 '.' 和 'X'
    # 这里假设原题中除 'X' 外是可放置位置，用 '.' 表示
    line_1 = [random.choice(['.', 'X']) for _ in range(n)]
    line_2 = [random.choice(['.', 'X']) for _ in range(n)]

    # 为了与原代码逻辑一致，转换为字符串再转回列表（可省略，此处保留风格）
    line_1 = [c for c in ''.join(line_1)]
    line_2 = [c for c in ''.join(line_2)]

    no = 0
    for i in range(len(line_1) - 1):
        if line_1[i] != 'X' and line_2[i] != 'X':
            if line_1[i + 1] != 'X':
                no += 1
                line_1[i] = 'X'
                line_2[i] = 'X'
                line_1[i + 1] = 'X'

            elif line_2[i + 1] != 'X':
                no += 1
                line_1[i] = 'X'
                line_2[i] = 'X'
                line_2[i + 1] = 'X'

        elif line_1[i] != 'X' and line_1[i + 1] != 'X' and line_2[i + 1] != 'X':
            no += 1
            line_1[i] = 'X'
            line_1[i + 1] = 'X'
            line_2[i + 1] = 'X'

        elif line_2[i] != 'X' and line_1[i + 1] != 'X' and line_2[i + 1] != 'X':
            no += 1
            line_2[i] = 'X'
            line_1[i + 1] = 'X'
            line_2[i + 1] = 'X'

    print(no)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)