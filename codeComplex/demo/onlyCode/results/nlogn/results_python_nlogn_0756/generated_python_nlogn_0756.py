def main(n):
    t = n
    res = []
    for _ in range(t):
        a = list(range(1, n + 1))[::-1]
        res.append(min(n - 2, a[1] - 1))
    return res

if __name__ == "__main__":
    print(main(5))