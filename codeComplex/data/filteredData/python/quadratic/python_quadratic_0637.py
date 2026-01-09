def main(n):
    l = sorted([(i * 2 + 3) for i in range(1, n + 1)])
    seen = [False] * n
    res = 0
    for i in range(n):
        if seen[i]:
            continue
        res += 1
        for j in range(i, n):
            if l[j] % l[i] == 0:
                seen[j] = True
    return res

if __name__ == "__main__":
    # print(main(10))
    pass