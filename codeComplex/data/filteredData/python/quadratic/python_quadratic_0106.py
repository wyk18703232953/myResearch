def main(n):
    N = n if n > 0 else 1

    # Deterministic generation of map_1 and map_2 as N x N character grids
    # Use simple arithmetic to create a pattern of 'A'..'Z'
    map_1 = [[chr(ord('A') + (i * N + j) % 26) for j in range(N)] for i in range(N)]
    map_2 = [[chr(ord('A') + ((N - 1 - i) * N + (N - 1 - j)) % 26) for j in range(N)] for i in range(N)]

    maps = list()

    maps.append([[map_2[i][j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[i][N - 1 - j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - i][j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - i][N - 1 - j] for j in range(N)] for i in range(N)])
    maps.append([[map_2[j][i] for j in range(N)] for i in range(N)])
    maps.append([[map_2[j][N - 1 - i] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - j][i] for j in range(N)] for i in range(N)])
    maps.append([[map_2[N - 1 - j][N - 1 - i] for j in range(N)] for i in range(N)])

    # print(('No', 'Yes')[any(map_1 == el for el in maps)])
    pass
if __name__ == "__main__":
    main(5)