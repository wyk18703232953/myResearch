def main(n):
    # Interpret n as number of rows; columns m = n for scalability
    m = n
    # Deterministically generate an n x m binary matrix
    # a[i][j] is 0/1 based on a simple arithmetic rule
    a = [[(i * m + j) % 2 for j in range(m)] for i in range(n)]

    ignorable = [True] * n

    for i in range(m):
        cnt = 0
        for j in range(n):
            cnt += a[j][i]
        if cnt == 1:
            for j in range(n):
                if a[j][i]:
                    ignorable[j] = False

    if any(ignorable):
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(5)