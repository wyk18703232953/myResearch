import sys
import random

def main(n):
    # 随机生成满足题目限制的 a, b 测试数据
    # 限制条件：不同时 > 1，否则一定输出 NO 毫无意义
    # 同时排除题目中特判直接 NO 的组合
    possible_pairs = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a > 1 and b > 1:
                continue
            a0, b0 = a, b
            if a0 > b0:
                a0, b0 = b0, a0
            if n == 2 and (a0, b0) == (1, 1):
                continue
            if n == 3 and (a0, b0) == (1, 1):
                continue
            possible_pairs.append((a, b))

    if not possible_pairs:
        # 如果没有合法 (a, b)，则直接输出 NO 并返回
        print("NO")
        return

    a, b = random.choice(possible_pairs)

    a0, b0 = a, b
    if a0 > b0:
        a0, b0 = b, a

    if n == 2 and (a0, b0) == (1, 1):
        print('NO')
        return
    if n == 3 and (a0, b0) == (1, 1):
        print('NO')
        return
    if a > 1 and b > 1:
        print('NO')
        return

    mat = [['0' for _ in range(n)] for _ in range(n)]
    mat1 = [['1' for _ in range(n)] for _ in range(n)]
    if b == 1:
        for x in range(n - a):
            mat[x][x + 1] = '1'
            mat[x + 1][x] = '1'
    else:
        mat = mat1
        for x in range(n):
            mat[x][x] = '0'
        for x in range(n - b):
            mat[x][x + 1] = '0'
            mat[x + 1][x] = '0'

    print('YES')
    for x in range(n):
        print(''.join(mat[x]))


if __name__ == "__main__":
    # 示例：可在此处指定规模 n 做简单测试
    main(5)