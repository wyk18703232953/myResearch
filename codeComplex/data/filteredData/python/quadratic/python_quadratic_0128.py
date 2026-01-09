def main(n):
    from collections import defaultdict as dc

    # Generate deterministic m and list l based on n
    m = n * 2
    # Construct l so that numbers from 1..n appear repeatedly in cycles
    l = [(i % n) + 1 for i in range(m)]

    x = dc(int)
    p = 0
    for val in l:
        x[val] += 1
        f = 1
        for k in range(1, n + 1):
            if x[k] == 0:
                f = 0
                break
        if f:
            p += 1
            for k in range(1, n + 1):
                x[k] -= 1

    # print(p)
    pass
if __name__ == "__main__":
    main(5)