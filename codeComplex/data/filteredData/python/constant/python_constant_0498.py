def main(n):
    q = n
    results = []
    for i in range(q):
        a = i + 1
        b = (i * 2) + 3
        k = i + 2
        if a < b:
            a, b = b, a
        if a > k:
            results.append(-1)
        elif a % 2 == b % 2 != k % 2:
            results.append(k - 2)
        elif (a + b) % 2 != 0:
            results.append(k - 1)

        else:
            results.append(k)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)