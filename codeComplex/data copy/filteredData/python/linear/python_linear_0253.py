def main(n):
    # 通过 n 确定输入规模：nbColumn 和 h
    # 保证 nbColumn >= 3，h >= 0 且在合理范围内
    nbColumn = max(3, n + 2)
    h = n

    # 以下是原程序逻辑
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
    # 示例调用：可按需修改 n 以进行规模实验
    main(10)