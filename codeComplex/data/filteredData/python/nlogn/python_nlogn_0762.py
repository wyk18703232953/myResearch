def main(n):
    t = n
    results = []
    for case in range(t):
        cur_n = case + 2
        a = [((i * 3 + case) % (cur_n + 3)) for i in range(cur_n)]
        a.sort()
        if a[-2] > cur_n - 2:
            results.append(str(cur_n - 2))

        else:
            results.append(str(a[-2] - 1))
    # print("\n".join(results))
    pass
if __name__ == "__main__":
    main(10)