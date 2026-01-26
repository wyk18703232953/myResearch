def main(n):
    # n is the length of the array
    if n <= 0:
        return 0

    # Deterministically generate the input array of length n
    # Example pattern: arr[i] = (i % 5) + 1
    arr = [(i % 5) + 1 for i in range(n)]

    dp_arr = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp_arr[i][i] = (arr[i], 1, arr[i])

    def merge_small(c1, c2):
        if c1[1] == 1 and c2[1] == 1:
            if c1[0] == c2[0]:
                return (c1[0] + 1, 1, c1[0] + 1)

            else:
                return (c1[0], 2, c2[0])
        elif c1[1] == 2 and c2[1] == 1:
            if c1[2] == c2[0]:
                if c1[0] == c1[2] + 1:
                    return (c1[0] + 1, 1, c1[0] + 1)

                else:
                    return (c1[0], 2, c2[2] + 1)

            else:
                return (c1[0], 3, c2[2])

        elif c1[1] == 1 and c2[1] == 2:
            if c1[2] == c2[0]:
                if c2[2] == c2[0] + 1:
                    return (c2[2] + 1, 1, c2[2] + 1)

                else:
                    return (c2[0] + 1, 2, c2[2])

            else:
                return (c1[0], 3, c2[2])

        elif c1[1] == 2 and c2[1] == 2:
            if c1[2] == c2[0]:
                c1 = (c1[0], 2, c1[2] + 1)
                c2 = (c2[2], 1, c2[2])
                if c1[1] == 2 and c2[1] == 1:
                    if c1[2] == c2[0]:
                        if c1[0] == c1[2] + 1:
                            return (c1[0] + 1, 1, c1[0] + 1)

                        else:
                            return (c1[0], 2, c2[2] + 1)

                    else:
                        return (c1[0], 3, c2[2])

            else:
                return (c1[0], 4, c2[2])

    def merge_main(c1, c2):
        if c1[1] > 2:
            if c2[1] > 2:
                if c1[2] == c2[0]:
                    return (c1[0], c1[1] + c2[1] - 1, c2[2])

                else:
                    return (c1[0], c1[1] + c2[1], c2[2])

            else:
                if c2[1] == 1:
                    if c1[2] == c2[0]:
                        return (c1[0], c1[1], c2[2] + 1)

                    else:
                        return (c1[0], c1[1] + 1, c2[2])
                if c2[1] == 2:
                    if c1[2] == c2[0]:
                        if c1[2] + 1 == c2[2]:
                            return (c1[0], c1[1], c2[2] + 1)

                        else:
                            return (c1[0], c1[1] + 1, c2[2])

                    else:
                        return (c1[0], c1[1] + 2, c2[2])

        else:
            if c2[1] > 2:
                if c1[1] == 1:
                    if c1[2] == c2[0]:
                        return (c1[2] + 1, c2[1], c2[2])

                    else:
                        return (c1[2], c2[1] + 1, c2[2])

                if c1[1] == 2:
                    if c1[2] == c2[0]:
                        if c1[0] == c1[2] + 1:
                            return (c1[0] + 1, c2[1], c2[2])

                        else:
                            return (c1[0], c2[1] + 1, c2[2])

                    else:
                        return (c1[0], c2[1] + 2, c2[2])

            else:
                return merge_small(c1, c2)

    for i1 in range(1, n):
        for j1 in range(n - i1):
            for k1 in range(j1, j1 + i1):
                res = merge_main(dp_arr[j1][k1], dp_arr[k1 + 1][j1 + i1])
                if dp_arr[j1][j1 + i1] is None or dp_arr[j1][j1 + i1][1] > res[1]:
                    dp_arr[j1][j1 + i1] = res

    result = dp_arr[0][n - 1][1]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)