def main(n):
    # n: length of array a
    k = max(1, n // 3)  # window size derived deterministically from n
    a = [(i * 7 + 3) % 100 for i in range(n)]
    r = 0
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    for i in range(n - k + 1):
        for j in range(i + k, min(n + 1, i + 2 * k)):
            r = max(r, (s[j] - s[i]) / (j - i))
    # print(r)
    pass
if __name__ == "__main__":
    main(10)