def main(n):
    # Generate deterministic input: n intervals (x, l)
    # Example pattern: x = i, l = (i % 5) + 1
    ls = [[i, (i % 5) + 1] for i in range(n)]

    lsr = [[max(ls[i][0] - ls[i][1], 0), ls[i][0] + ls[i][1]] for i in range(n)]
    lsr.sort(key=lambda x: x[1])
    idx = 0
    ans = 0

    for l in lsr:
        if idx <= l[0]:
            idx = l[1]
            ans += 1

    print(ans)
    return ans

if __name__ == "__main__":
    main(10)