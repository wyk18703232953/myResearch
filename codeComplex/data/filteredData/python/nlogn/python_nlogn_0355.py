def main(n):
    # n is the length of the list x
    # Deterministically generate x: a simple arithmetic progression
    # including some powers-of-two spaced values to allow matches
    x = [i for i in range(1, n + 1)]
    s = set(x)
    ans = [x[0]]
    for i in range(n):
        for j in range(0, 32):
            val1 = x[i] + (1 << j)
            if val1 in s:
                ans = [x[i], val1]
                val2 = x[i] + (2 << j)
                if val2 in s:
                    ans.append(val2)
                    print(len(ans))
                    print(*ans)
                    return
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main(10)