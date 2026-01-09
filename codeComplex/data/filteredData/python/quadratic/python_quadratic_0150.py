def main(n):
    lst1 = []
    for x in range(n):
        row = ''.join('0' if (x + y) % 3 == 0 else '1' for y in range(n))
        lst1.append([row])

    s = "separator_1"

    lst2 = []
    for x in range(n):
        row = ''.join('1' if (x * 2 + y) % 3 == 1 else '0' for y in range(n))
        lst2.append([row])

    s = "separator_2"

    lst3 = []
    for x in range(n):
        row = ''.join('0' if (x + 2 * y) % 3 == 2 else '1' for y in range(n))
        lst3.append([row])

    s = "separator_3"

    lst4 = []
    for x in range(n):
        row = ''.join('1' if (x * x + y) % 2 == 0 else '0' for y in range(n))
        lst4.append([row])

    ans_b1 = 0
    ans_w1 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst1[x][0][y] == '0':
                    ans_b1 += 1

                else:
                    ans_w1 += 1

            else:
                if lst1[x][0][y] == '1':
                    ans_b1 += 1

                else:
                    ans_w1 += 1

    ans_b2 = 0
    ans_w2 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst2[x][0][y] == '0':
                    ans_b2 += 1

                else:
                    ans_w2 += 1

            else:
                if lst2[x][0][y] == '1':
                    ans_b2 += 1

                else:
                    ans_w2 += 1

    ans_b3 = 0
    ans_w3 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst3[x][0][y] == '0':
                    ans_b3 += 1

                else:
                    ans_w3 += 1

            else:
                if lst3[x][0][y] == '1':
                    ans_b3 += 1

                else:
                    ans_w3 += 1

    ans_b4 = 0
    ans_w4 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst4[x][0][y] == '0':
                    ans_b4 += 1

                else:
                    ans_w4 += 1

            else:
                if lst4[x][0][y] == '1':
                    ans_b4 += 1

                else:
                    ans_w4 += 1

    result = (2 * n) ** 2 - max(
        ans_b1 + ans_b2 + ans_w3 + ans_w4,
        ans_b1 + ans_w2 + ans_b3 + ans_w4,
        ans_b1 + ans_w2 + ans_w3 + ans_b4,
        ans_w1 + ans_b2 + ans_b3 + ans_w4,
        ans_w1 + ans_b2 + ans_w3 + ans_b4,
        ans_w1 + ans_w2 + ans_b3 + ans_b4,
    )
    # print(result)
    pass
if __name__ == "__main__":
    main(10)