def main(n):
    N = max(1, int(n))

    # 确定性生成 map_1 和 map_2
    map_1 = []
    map_2 = []
    for i in range(N):
        row1 = []
        row2 = []
        for j in range(N):
            # 使用简单算术构造字符，保证确定性
            ch1 = chr(ord('A') + (i + j) % 26)
            ch2 = chr(ord('A') + (i * 2 + j * 3) % 26)
            row1.append(ch1)
            row2.append(ch2)
        map_1.append(row1)
        map_2.append(row2)

    maps = []
    maps.append([[map_2[i][j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[i][N - 1 - j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - i][j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - i][N - 1 - j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[j][i] for j in range(N)] for i in range(N)])
    maps.append([[map_2[j][N - 1 - i] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - j][i] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - j][N - 1 - i] for j in range(N)] for i in range(N)])

    result = ('No', 'Yes')[any(map_1 == el for el in maps)]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(5)