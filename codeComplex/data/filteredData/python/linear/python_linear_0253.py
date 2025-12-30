import random

def main(n):
    # 生成测试数据：根据规模 n 生成 nbColumn 和 h
    # 这里约定：列数 nbColumn = n，h 在 [0, 2*(nbColumn-2)] 内随机生成，
    # 确保既有可能输出 YES 也有可能输出 NO
    nbColumn = max(3, n)  # 至少 3 列以匹配原逻辑的意义
    max_h = max(0, 2 * (nbColumn - 2))
    h = random.randint(0, max_h)

    # 输出生成的测试数据（如不需要可注释掉）
    print(nbColumn, h)

    # 下面是原逻辑
    if (nbColumn - 2) * 2 < h:
        print('NO')
    else:
        print('YES')
        if h % 2 == 0:
            print('.' * nbColumn)
            print('.' + '#' * (h // 2) + '.' * (nbColumn - 1 - h // 2))
            print('.' + '#' * (h // 2) + '.' * (nbColumn - 1 - h // 2))
            print('.' * nbColumn)
        else:
            print('.' * nbColumn)
            hFirst = min(h, nbColumn - 2)
            countPoint = (nbColumn - hFirst) // 2
            print('.' * countPoint + '#' * hFirst + '.' * countPoint)
            hSecond = (h - hFirst) // 2
            countPoint = nbColumn - 2 * hSecond - 2
            print('.' + '#' * hSecond + '.' * countPoint + '#' * hSecond + '.')
            print('.' * nbColumn)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)