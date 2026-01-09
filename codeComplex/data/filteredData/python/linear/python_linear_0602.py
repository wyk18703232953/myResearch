def main(n):
    k = n // 3
    ans = []
    for i in range(k):
        ans += [(0, 2 * i)]
        ans += [(1, 2 * i + 1)]
        ans += [(2, 2 * i)]
    for i in range(n % 3):
        ans += [(-1000, -1000 + i)]
    res = ""
    for i in ans:
        res += " ".join(map(str, i)) + "\n"
    # print(res)
    pass
if __name__ == "__main__":
    main(10)