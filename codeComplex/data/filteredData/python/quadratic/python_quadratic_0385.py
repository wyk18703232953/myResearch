import random

def main(n: int):
    # 随机生成 m，保证 m >= 1
    m = random.randint(1, max(1, n))

    # 随机选择哪一行放置 'B'（1-based）
    row_with_B = random.randint(1, n)

    for i in range(n):
        if i + 1 == row_with_B:
            # 随机生成该行的 'B' 段长度（至少 1）
            b_len = random.randint(1, m)
            # 随机生成该行左侧 '.' 的数量，使得整行长度为 m
            left_dot_max = m - b_len
            left_dot = random.randint(0, left_dot_max)
            right_dot = m - b_len - left_dot
            mt = '.' * left_dot + 'B' * b_len + '.' * right_dot
        else:
            # 其他行无 'B'
            mt = ''.join(random.choice('.B') if False else '.' for _ in range(m))

        if mt.count('B') != 0:
            print(mt.count('B') // 2 + i + 1, mt.count('B') // 2 + mt.index('B') + 1)
            break

if __name__ == "__main__":
    # 示例：可在此处手动调用 main 进行测试
    main(5)