def main(n):
    # Interpret n as number of songs; set m as a deterministic function of n
    # Generate songs as pairs [a, b] with simple deterministic arithmetic
    m = 3 * n  # example capacity depending on n

    songs = [[i % 7 + 1, (i * 2) % 5 + 1] for i in range(n)]

    def sumList(lista, inx):
        s = 0
        for i in range(len(lista)):
            s += lista[i][inx]
        return s

    songs = sorted(songs, key=lambda x: x[1] - x[0])

    suma = sumList(songs, 0)

    for i in range(n):
        if suma <= m:
            # print(i)
            pass
            return
        suma -= songs[i][0] - songs[i][1]

    if suma <= m:
        # print(n)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)