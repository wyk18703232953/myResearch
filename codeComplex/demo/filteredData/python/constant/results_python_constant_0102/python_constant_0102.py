def main(n):
    t = n
    results = []
    for i in range(1, t + 1):
        a = i
        b = i * 2 + 1
        ans = 0
        while a and b:
            a, b = min(a, b), max(a, b)
            ans, b = ans + b // a, b % a
        results.append(ans)
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)