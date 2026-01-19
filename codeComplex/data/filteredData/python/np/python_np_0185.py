from itertools import combinations

def main(n):
    # Deterministically generate parameters based on n
    # n is the length of the list c
    if n < 2:
        print(0)
        return

    c = [i * 2 + 1 for i in range(n)]  # strictly increasing odd numbers
    c.sort()

    total_sum = sum(c)
    l = total_sum // 4 if total_sum // 4 > 0 else 1
    r = (total_sum * 3) // 4 if (total_sum * 3) // 4 >= l else l
    x = max(1, c[-1] // 3)

    k = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (c[j] - c[i]) >= x:
                if sum(c[i:j + 1]) < l:
                    continue
                elif (c[i] + c[j]) > r:
                    continue
                else:
                    if (c[i] + c[j]) >= l and (c[i] + c[j]) <= r:
                        k += 1
                    for p in range(1, j - i):
                        for m in combinations(c[i + 1:j], p):
                            s = sum(m) + c[i] + c[j]
                            if s >= l and s <= r:
                                k += 1

    print(k)


if __name__ == "__main__":
    main(10)