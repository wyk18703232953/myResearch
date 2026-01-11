def main(n):
    # n controls the number of pairs
    if n <= 0:
        return

    # Deterministically construct m and the list of (a, b) pairs
    # Example scheme:
    #   m grows roughly like sum of b plus some margin depending on n
    #   a[i] = i + 2
    #   b[i] = i % 3
    final = []
    s2 = 0
    for i in range(n):
        a = i + 2
        b = i % 3
        final.append([a, b])
        s2 += b

    # Set m so that the behavior depends on n but is deterministic
    m = s2 + n // 2

    final.sort(key=lambda x: x[0] - x[1])

    s1 = 0
    s2 = 0
    for i in final:
        s2 += i[1]
        s1 += i[0]

    if s2 > m:
        # print(-1)
        pass

    else:
        if s1 <= m:
            # print(0)
            pass

        else:
            i = n - 1
            count = 0
            while s1 > m and i >= 0:
                s1 = s1 - (final[i][0] - final[i][1])
                count += 1
                i -= 1
            # print(count)
            pass
if __name__ == "__main__":
    main(10)