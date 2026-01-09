def main(n):
    # 根据 n 确定 nbColumn 和 h 的规模
    # 保证 nbColumn >= 3，避免原题中 (nbColumn-2) 的退化情况
    nbColumn = max(3, n)
    # 让 h 在 [0, 2*(nbColumn-2)] 范围内变化，便于既有 NO 又有 YES 情况
    h = (3 * n) % (2 * max(1, (nbColumn - 2)) + 1)

    if (nbColumn - 2) * 2 < h:
        # print('NO')
        pass

    else:
        # print('YES')
        pass

        if h % 2 == 0:
            # print('.' * nbColumn)
            pass
            # print('.' + '#' * (h // 2) + '.' * (nbColumn - 1 - h // 2))
            pass
            # print('.' + '#' * (h // 2) + '.' * (nbColumn - 1 - h // 2))
            pass
            # print('.' * nbColumn)
            pass

        else:
            # print('.' * nbColumn)
            pass
            hFirst = min(h, nbColumn - 2)
            countPoint = (nbColumn - hFirst) // 2
            # print('.' * countPoint + '#' * hFirst + '.' * countPoint)
            pass
            hSecond = (h - hFirst) // 2
            countPoint = nbColumn - 2 * hSecond - 2
            # print('.' + '#' * hSecond + '.' * countPoint + '#' * hSecond + '.')
            pass
            # print('.' * nbColumn)
            pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以进行规模化实验
    main(10)