def main(n):
    x = n
    y = n // 2
    z = (3 * n) // 4
    t1 = 2
    t2 = 3
    t3 = 5
    elev = t3 * 3 + t2 * (abs(z - x) + abs(x - y))
    stairs = t1 * abs(x - y)
    if elev <= stairs:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(1000)