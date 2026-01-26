from collections import Counter

def main(n):
    # n: number of items to be distributed
    # m: number of distinct types (mapped from n deterministically)
    m = max(1, n // 2)

    # Generate m items deterministically as strings, repeated to ensure enough total count
    # We want total count >= n to make the problem meaningful
    base_items = [str(i % m) for i in range(max(n, m))]
    items = base_items[:n]

    c = Counter(items).values()
    d = 1
    while sum(ci // d for ci in c) >= n:
        d += 1
    result = d - 1
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)