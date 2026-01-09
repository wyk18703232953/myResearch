def main(n):
    # Interpret n as number of rows; derive m deterministically from n
    m = max(1, n // 2)

    tc = [0] * m
    ps = []

    # Deterministically generate n binary strings of length m
    # temp[i] is '1' if (row_index + i) is even, else '0'
    for row in range(n):
        temp = ''.join('1' if (row + col) % 2 == 0 else '0' for col in range(m))
        psa = [0] * m
        for i in range(m):
            if temp[i] == '1':
                psa[i] += 1
                tc[i] += 1
        ps.append(psa)

    ans = 'NO'
    for i in ps:
        c = 0
        for j in range(m):
            if tc[j] - i[j] > 0:
                c += 1
        if c == m:
            ans = 'YES'
            break

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)