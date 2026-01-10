def main(n):
    from collections import Counter

    # Interpret n as the number of items; p is derived deterministically from n
    p = max(1, n // 3)

    # Deterministically generate the list that originally came from input
    # Example pattern: sequence of values cycling from 1 to max(1, n//5)
    max_val = max(1, n // 5)
    arr = [(i % max_val) + 1 for i in range(n)]

    d = Counter(arr)

    def pos(required_count):
        t = 0
        for _, v in d.items():
            if v >= required_count:
                t += v // required_count
        return t >= p

    ans = 0
    for sel in range(1, n + 1):
        if pos(sel):
            ans = max(ans, sel)

    print(ans)


if __name__ == "__main__":
    main(1000)