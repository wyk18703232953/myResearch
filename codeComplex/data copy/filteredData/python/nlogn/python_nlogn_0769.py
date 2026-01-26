def main(n):
    c = n
    results = []
    for i in range(c):
        cur_n = max(2, n)
        s = [(j * 2 + i) % (2 * n + 3) + 1 for j in range(cur_n)]
        s.sort()
        l = min(s[-1], s[-2])
        ans = min(l - 1, cur_n - 2)
        results.append(ans)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)