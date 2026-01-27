def main(n):
    results = []
    for _ in range(n):
        a = _ + 1
        b = 2 * _ + 3
        result = 0
        while min(a, b) != 0:
            x = max(a, b)
            y = min(a, b)
            a = x
            b = y
            result += a // b
            a %= b
        results.append(result)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)