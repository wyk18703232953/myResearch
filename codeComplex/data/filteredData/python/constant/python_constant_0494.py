def main(n):
    q = n
    results = []
    for e in range(q):
        x = e
        y = n - e
        k = e + n
        x, y = abs(x), abs(y)
        x, y = max(x, y), min(x, y)

        if (x % 2 != k % 2):
            k -= 1
            y -= 1

        if x > k:
            results.append(-1)
            continue
        if (x - y) % 2:
            k -= 1
            x -= 1
        results.append(k)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)