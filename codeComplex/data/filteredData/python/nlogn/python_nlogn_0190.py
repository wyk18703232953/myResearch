def main(n):
    # Generate deterministic input:
    # Original program expects:
    # n: length of list
    # l: list of n integers
    # Here we map n directly to list length, and generate l deterministically.
    l = [(i * 3 + 1) % (n // 2 + 1 if n > 1 else 1) for i in range(n)]

    d = {}
    for i in l:
        d[i] = 0
    total_sum = 0
    fre = 0
    ans = 0
    for i in range(n - 1, -1, -1):
        x = total_sum
        y = fre
        for j in range(-1, 2):
            aa = l[i] + j
            if aa in d:
                x -= aa * d[aa]
                y -= d[aa]
        ans += x - l[i] * y
        fre += 1
        total_sum += l[i]
        d[l[i]] += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)