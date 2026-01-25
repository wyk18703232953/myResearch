def main(n):
    # Generate deterministic input data based on n
    # a and b are permutations of [1..n]
    a = list(range(1, n + 1))
    b = list(range(n, 0, -1))

    done = set()
    j = 0
    ans = []
    for i in range(n):
        if b[i] in done:
            ans.append(0)
        else:
            c = 0
            while a[j] != b[i]:
                done.add(a[j])
                j += 1
                c += 1
            done.add(a[j])
            j += 1
            ans.append(c + 1)

    print(*ans)


if __name__ == "__main__":
    main(10)