def main(n):
    # Interpret n as the number of songs
    # Deterministically generate m and songs
    # m grows roughly proportional to n to keep behavior non-trivial
    m = n * (n // 2 + 1)

    # Generate songs as a list of [a, b]
    # a and b are simple deterministic functions of index i
    songs = []
    for i in range(n):
        a = (i * 3) % (n + 5) + i // 2
        b = (i * 5) % (n + 7) + i // 3
        songs.append([a, b])

    def sumList(lista, inx):
        s = 0
        for i in range(len(lista)):
            s += lista[i][inx]
        return s

    songs_sorted = sorted(songs, key=lambda x: x[1] - x[0])
    suma = sumList(songs_sorted, 0)

    for i in range(n):
        if suma <= m:
            print(i)
            return
        suma -= songs_sorted[i][0] - songs_sorted[i][1]

    if suma <= m:
        print(n)
    else:
        print(-1)


if __name__ == "__main__":
    main(10)