def main(n):
    # Deterministically generate input array 'a' of length n
    # Example pattern: a[i] = (i * 3 + 1) % (2 * n + 1)
    a = [(i * 3 + 1) % (2 * n + 1) for i in range(n)]

    k = [i for i in a]
    lst = []
    for i in range(n):
        p = k[i] % n
        ans = 0
        rotated = k[i + 1:] + k[:i + 1]
        rotated[-1] = 0
        base = k[i] // n
        for j in range(n):
            if (rotated[j] + 1 + base) % 2 == 0 and j < p:
                ans += rotated[j] + 1 + base
            elif (rotated[j] + base) % 2 == 0 and j >= p:
                ans += rotated[j] + base
        lst.append(ans)

    result = max(lst) if lst else 0
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)