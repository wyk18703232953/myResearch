def main(n):
    import random
    import math
    k = max(1, min(n, n // 2 + 1))
    t = []
    for _ in [0] * n:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        t.append([a, b])
    t.sort(key=lambda x: (-x[0], x[1]))
    pt = t[k - 1]
    return t.count(pt)

if __name__ == "__main__":
    print(main(10))